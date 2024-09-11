from fastapi import FastAPI
from psgrsdb.models import Base
from psgrsdb.database import engine
from psgrsdb.routes.routes import router
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)


