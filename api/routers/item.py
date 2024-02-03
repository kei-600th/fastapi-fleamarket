from typing import Optional
from fastapi import APIRouter, Path
from api.cruds import item as item_cruds
from api.schemas import item as item_schemas


router = APIRouter(prefix="/items", tags=["Items"])


@router.get("", response_model=list[item_schemas.ItemResponse])
async def find_all():
    return item_cruds.find_all()


@router.get("/{id}", response_model=Optional[item_schemas.ItemResponse])
async def find_by_id(id: int = Path(gt=0)):
    return item_cruds.find_by_id(id)


@router.get("/", response_model=list[item_schemas.ItemResponse])
async def find_by_name(name: str):
    return item_cruds.find_by_name(name)


@router.post("", response_model=item_schemas.ItemResponse)
async def create(item_create: item_schemas.ItemCreate):
    return item_cruds.create(item_create)


@router.put("/{id}", response_model=Optional[item_schemas.ItemResponse])
async def update(item_update: item_schemas.ItemUpdate, id: int = Path(gt=0)):
    return item_cruds.update(id, item_update)


@router.delete("/{id}", response_model=Optional[item_schemas.ItemResponse])
async def delete(id: int = Path(gt=0)):
    return item_cruds.delete(id)
