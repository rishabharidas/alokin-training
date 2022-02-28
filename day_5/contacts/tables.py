from databasedata import engine
from sqlalchemy import Column, Integer, ForeignKey, Text, VARCHAR
from sqlalchemy.orm import declarative_base

table_base = declarative_base()

class contactstable(table_base):
    __tablename__ = 'contactstable'
    name = Column(VARCHAR(25), primary_key=True)
    notes = Column(Text)
    emails = Column(Text)
    phones = Column(Text)
    jobDetails = Column(Text)

table_base.metadata.create_all(engine)
