from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql://bnpfsdon:JsBIfb1hA22GTTLxMFmUomDWwvNt_vBg@mel.db.elephantsql.com/bnpfsdon'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
# # SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:12345@localhost/TodoAppDatabase'
# # SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:123456@127.0.0.1/todoapp'
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()