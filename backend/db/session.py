from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import PostgresDsn

SQLALCHEMY_DATABASE_URI = PostgresDsn.build(
    scheme="postgresql",
    user="POSTGRES_USER",
    password="POSTGRES_PASSWORD",
    host="POSTGRES_SERVER",
    path=f"/{'POSTGRES_DB' or ''}",
)
engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
try:
    db = SessionLocal()
    db.execute("SELECT 1")
except Exception as e:
    raise e