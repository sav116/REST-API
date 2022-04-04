from typing import List
from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from db.db_session import get_db
from db.items import Item as dbItem
from models.items import Item
from endpoints.base import prefix

router = APIRouter(prefix=prefix)


@router.get("/items", status_code=status.HTTP_200_OK)
async def get_all(db: Session = Depends(get_db)):
    return db.query(dbItem).all()


@router.get('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
async def get_by_id(item_id: int,
                    db: Session = Depends(get_db)):
    return db.query(dbItem).filter(dbItem.id == item_id).first()


@router.post('/items', response_model=Item,
             status_code=status.HTTP_201_CREATED)
async def create(item: Item,
                 db: Session = Depends(get_db)):
    db_item = db.query(dbItem).filter(dbItem.name == item.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail="Item already exists")

    new_item = dbItem(
        name=item.name,
        price=item.price,
        description=item.description,
        on_offer=item.on_offer
    )

    db.add(new_item)
    db.commit()

    return new_item


@router.put('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
async def update(item_id: int,
                 item: Item,
                 db: Session = Depends(get_db)):
    item_to_update = db.query(dbItem).filter(dbItem.id == item_id).first()
    item_to_update.name = item.name
    item_to_update.price = item.price
    item_to_update.description = item.description
    item_to_update.on_offer = item.on_offer

    db.commit()

    return item_to_update


@router.delete('/item/{item_id}')
async def delete(item_id: int,
                 db: Session = Depends(get_db)):
    item_to_delete = db.query(dbItem).filter(dbItem.id == item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    db.delete(item_to_delete)
    db.commit()

    return item_to_delete
