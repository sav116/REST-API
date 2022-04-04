from db.base import Base
from sqlalchemy.dialects.postgresql import UUID, TEXT, TIMESTAMP, INTEGER, BOOLEAN
from sqlalchemy import Column, MetaData

metadata = MetaData()


class Item(Base):
    __tablename__ = 'items'
    metadata = metadata
    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT)
    description = Column(TEXT)
    price = Column(INTEGER)
    on_offer = Column(BOOLEAN)
