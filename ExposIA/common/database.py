import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/exposia.db")

if DATABASE_URL.startswith("sqlite"):
    path = DATABASE_URL.replace("sqlite:///", "")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    connect_args = {"check_same_thread": False}
else:
    connect_args = {}

engine = create_engine(DATABASE_URL, echo=False, future=True, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def init_db():
    """Create tables."""
    Base.metadata.create_all(engine)
