
from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from api.logics.base import CRUDBase
from api import models, schemas


class Item(CRUDBase[models.Item, schemas.ItemCreate, schemas.ItemUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: schemas.ItemCreate, owner_id: int
    ) -> models.Item:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[models.Item]:
        return (
            db.query(self.model)
            .filter(models.Item.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


item = Item(models.Item)
