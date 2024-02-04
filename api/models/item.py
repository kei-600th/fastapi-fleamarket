from datetime import datetime
from api.database import Base
from sqlalchemy import Column, Integer, String, Enum, DateTime
from api.schemas import item as item_schemas


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(item_schemas.ItemStatus), nullable=False,
                    default=item_schemas.ItemStatus.ON_SALE)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(),
                        onupdate=datetime.now())
