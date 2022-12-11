from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Make the conection
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:M@ps5250864POST@lochasthost:5432/fastAPI_database"

# engine: Interact with DB
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Know how is the data
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Declarative base: To start to create our models
Base = declarative_base()