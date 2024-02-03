from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class ItemStatus(Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"


class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=20, examples=["PC"])
    price: int = Field(gt=0, examples=[10000])
    description: Optional[str] = Field(None, examples=["美品です"])


class ItemUpdate(BaseModel):
    name: Optional[str] = Field(min_length=2, max_length=20, examples=["PC"])
    price: Optional[int] = Field(gt=0, examples=[10000])
    description: Optional[str] = Field(None, examples=["美品です"])
    status: Optional[ItemStatus] = Field(None, examples=[ItemStatus.SOLD_OUT])
