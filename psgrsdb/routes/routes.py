from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from psgrsdb import schemas 
from psgrsdb import models
import bcrypt
import asyncio
from ..auth.auth import create_token, token_check
from fastapi import Depends, APIRouter
from ..data_dicts.data_dicts import update_dict, model_dict
from ..database import Session as dbSession
###Router Setup###

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
def get_db():
    db = dbSession
    try:
        yield db
    finally:
        db.close()
        
##Helper Functions###
async def been_updated(updateArr, db: Session = Depends(get_db)):
    
    for x in updateArr:
        db_is_updated = db.query(models.Singleton).join(update_dict[x]).first()
        db_is_updated.is_updated = True
        db.commit()
        db.refresh(db_is_updated)

async def needs_updated(updateArr, db: Session = Depends(get_db)):
    for x in updateArr:
        db_is_updated = db.query(models.Singleton).join(update_dict[x]).first()
        db_is_updated.is_updated = False
        db.commit()
        db.refresh(db_is_updated)

async def content_array(contentObj,contentStr, db):
    key_arr = list(contentObj.keys())
    obj = {
            contentStr : {}
        }
    for x in key_arr:
        tableLoc = contentObj[x]['model']
        content_list = await db.query(tableLoc).filter(tableLoc.to_be_updated == True).all()
        schemad_list = []
        for item in content_list:
            schemad_list.append(contentObj[x]["schema"]["get"].from_orm(item))
            item.to_be_updated = False
            await db.commit()
            db.refresh(item)
        content_sorted = sorted(schemad_list, key=lambda x: x.id)
        obj[contentStr][x] = content_sorted
    return obj

###Routes###
@router.post("/initadmin", response_model = None)
async def create_admin(
    post: schemas.user.UserCreate,
    db : Session = Depends(get_db)
    ):
    singleton = db.query(models.Singleton).first()
    if not singleton:
        singleton = models.Singleton(id = 1)
        db.add(singleton)
        db.commit()
        db.refresh(singleton)
        update = models.Update(id = 1, singleton_id = singleton.id)
        db.add(update)
        db.commit()
        db.refresh(update)
        ml_update = models.ML_Update(id = 1, singleton_id = singleton.id)
        db.add(ml_update)
        db.commit()
        db.refresh(ml_update)

    
    db_check = db.query(models.Admin).all()
    print(db_check)
    if db_check:
        return "Admin already exists"
    db_singleton = db.query(models.Singleton).first()
    password_hash = post.password_hash
    username = post.username
    db_admin = models.Admin(id = 1, username = username, password_hash = password_hash, singleton_id = db_singleton.id)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    await needs_updated(["gen"], db = db)
    return "created"

@router.post("/auth")
async def authenticate(admin: schemas.UserLogin, db: Session = Depends(get_db)):
    db_admin = await db.query(models.Admin).filter(models.Admin.username == admin.username).first()
    if db_admin == None:
        return "User not Found"
    #User not found
    if bcrypt.checkpw(admin.password.encode('utf-8'), db_admin.password_hash):
        token_payload = schemas.Token({"role" : "admin"})
        return create_token(token_payload)
    #Password Correct
    else:
        return "Invalid password"
    #Password Incorrect
@router.get("/")
async def check_if_updated(db: Session = Depends(get_db)):
    update_arr = list(update_dict.keys())
    update_obj = {"updates_required" : []}
    for item in update_arr:
        update_bool = await db.query(models.Singleton).join(update_dict[item]).first()
        update_obj["updates_required"].append({item : update_bool.is_updated})
    return update_obj

@router.get("/get")
async def get_content(db: Session = Depends(get_db)):
    data_object = {"content" : {}}
    updateArr = []
    for category in model_dict.keys():
        updateArr.append(category)
        data_object["content"] = await content_array(model_dict[category], category, db)
    updateables = await db.query(models.Singleton).join(models.Singleton.Updateables).first()
    if updateables.to_be_updated == True:
        data_object["content"]["gen"]["updateables"] = schemas.UpdateableGet(updateables)
        updateables.to_be_updated = False
        await db.commit()
        db.refresh(updateables)
    been_updated(updateArr)
    return data_object

@router.delete("/del/{category}/{table}/")
async def delete_content_master(table: str, id: int, category: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    if not await token_check(token):
        return "Just because you have audacity does not mean you have authority. Bugger off." 
    async def delete_content(table_str, id, content_type, db: Session = Depends(get_db)):

        super_category = content_type
        model = model_dict[super_category][table_str]["model"]
        schema_class = model_dict[super_category][table_str]["schema"]["delete"]
        schema = schema_class(id=id)
        db_content = await db.query(model).filter(model.id == schema.id).first()
        
        db_content.to_be_deleted = True
        db_content.to_be_updated = True
        await db.commit()
        await needs_updated(x = content_type)
        db.refresh(db_content)
        return db_content
    
    async def resolve_deletion(db_content):
        db.delete(db_content)
        await db.commit()
        db.refresh()
        return "Content deleted"

    deleted_content = delete_content(table, id, category)
    await asyncio.sleep(3)
    return resolve_deletion(deleted_content)

@router.post("/create/{category}/{table}")
async def create_content(category:str, table:str, postObject, token: str =Depends(oauth2_scheme), db: Session = Depends(get_db)):
    if not token_check(token):
        return "Just because you have audacity does not mean you have authority. Bugger off."

    model = model_dict[category][table].model
    schema = model_dict[category][table].schema.create
    schema_instance = schema(**postObject)
    model_instance = model(**schema_instance.model_dump())
    db.add(model_instance)
    await needs_updated([category])
    await db.commit()
    db.refresh(model_instance)
    return {"new database entry" : model_instance}

@router.put("/update/{category}/{table}/")
async def update_content(table, category, updateObject, token: str=Depends(oauth2_scheme), db : Session = Depends(get_db)):
    if not token_check(token):
        return "Just because you have audacity does not mean you have authority. Bugger off."
    model = model_dict[category][table].model
    schema = model_dict[category][table].schema.update
    schema_instance = schema(**updateObject)
    updating_content = await db.query(model).filter(model.id == schema_instance.id).first()
    if updating_content:
        for key, value in schema_instance.model_dump().items():
            setattr(updating_content, key, value)
            updating_content.to_be_updated = True
            await needs_updated(category)
            await db.commit()
            db.refresh(updating_content)
        return {"updated content" : schema_instance}
    else:
        return {"error": "Content not found"}
    









