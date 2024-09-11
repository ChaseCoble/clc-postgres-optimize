from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.ext.declarative import AbstractConcreteBase

class PortfolioItems(Base):
    __tablename__ = 'portfolio_items'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    date = Column(String(255))
    category = Column(String(255))
    detail = Column(String(255))
    img_URL = Column(String(255))
    repo_URL = Column(String(255))
    language = Column(String(255))
    framework = Column(String(255))
    deploy_URL = Column(String(255))
    to_be_updated = Column(Boolean, default = True)
    to_be_deleted = Column(Boolean, default = False)
class Articles(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    date = Column(String(255))
    content = Column(String(255))
    topic = Column(String(255))
    img_URL = Column(String(255))
    vid_URL = Column(String(255))
    references = Column(JSONB)
    to_be_updated = Column(Boolean)
    to_be_deleted = Column(Boolean)



class Career(Base):
    __tablename__ = 'career'
    id = Column(Integer, primary_key=True)
    start_title = Column((String(255)))
    end_title = Column((String(255)))
    employer = Column(String(255))
    start_date = Column(String(255))
    end_date = Column(String(255))
    description = Column(String(255))
    to_be_updated = Column(Boolean)
    to_be_deleted = Column(Boolean)

class Education(Base):
    __tablename__ = 'education'
    id = Column(Integer, primary_key=True)
    merit = Column(String(255))
    source = Column(String(255))
    completion_date = Column(String(255))
    details = Column(String(255))
    to_be_updated = Column(Boolean)
    to_be_deleted = Column(Boolean)

class Links(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    url = Column(String(255))
    logo_url = Column(String(255))
    to_be_updated = Column(Boolean)
    to_be_deleted = Column(Boolean)

class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    level = Column(Integer)
    symbol = Column(String(255))
    category = Column(String(255))
    #WebDev, Data Science, Software
    to_be_updated = Column(Boolean)
    to_be_deleted = Column(Boolean)

class Regression(Base):
    __tablename__ = 'regression'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    axis_x = Column(String(255))
    axis_y = Column(String(255))
    x = Column(ARRAY(Float))
    y = Column(ARRAY(Float))
    acc = Column(Float)
    corr = Column(Float)
    slope = Column(Float)
    intercept = Column(Float)
    data_date = Column(String(255))
    to_be_updated = Column(Boolean)
    to_be_deleted = Column(Boolean)

class KNeighbors(Base):
    __tablename__ = 'kneighbors'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    centers = Column(ARRAY(Float))
    categories = Column(ARRAY(String))
    cat_Ids = Column(ARRAY(Integer))
    data_date = Column(String(255))
    obj = Column(ARRAY(Float)) #Format [[catId, x, y, z],[...]]
    to_be_updated = Column(Boolean)
    to_be_deleted = Column(Boolean)

class Graphing(Base):
    __tablename__ = 'graphing'
    id = Column(Integer, primary_key= True)
    title = Column(String(255))
    axis_x = Column(String(255))
    axis_y = Column(String(255))
    x = Column(ARRAY(Float))
    y = Column(ARRAY(Float))
    graph_type = Column(String(255))


class Singleton(Base):
    __tablename__ = 'singleton'
    id = Column(Integer, primary_key=True, unique=True)
    admin = relationship("Admin", uselist = False,  back_populates="singleton")
    update = relationship("Update",  uselist = False,  back_populates="singleton")
    updateables = relationship("Updateables",  uselist=False, back_populates="singleton")
    ml_update = relationship("ML_Update",  uselist = False, back_populates = "singleton")
class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    password_hash = Column(String(255))
    singleton_id = Column(Integer, ForeignKey('singleton.id'))
    singleton = relationship("Singleton", uselist=False, back_populates = "admin")

class Update(Base):
    __tablename__ = 'update'
    id = Column(Integer, primary_key=True)
    is_updated = Column(Boolean, default=True)
    singleton_id = Column(Integer, ForeignKey('singleton.id'))
    singleton = relationship("Singleton", uselist=False, back_populates="update")

class ML_Update(Base):
    __tablename__ ='ml_update'
    id = Column(Integer, primary_key = True)
    is_updated = Column(Boolean, default=True)
    singleton_id = Column(Integer, ForeignKey('singleton.id'))
    singleton = relationship("Singleton", uselist=False, back_populates="ml_update")

class Updateables(Base):
    __tablename__ = 'updateables'
    id = Column(Integer, primary_key=True)
    phone = Column(String(255))
    email = Column(String(255))
    contact_Pic = Column(String(255))
    bio_Blurb = Column(String(255))
    logo = Column(String(255))
    home_Img = Column(String(255))
    cv_Img = Column(String(255))
    address = Column(String(255))
    to_be_updated = Column(Boolean)
    singleton_id = Column(Integer, ForeignKey('singleton.id'))
    singleton = relationship("Singleton", uselist=False, back_populates = 'updateables')

Base.registry.configure()