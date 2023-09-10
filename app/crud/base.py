# Copyright 2023 Marin Pejcin


from typing import Any, Dict, List, Optional, Type, TypeVar, Generic, Union
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.database import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**

        * model: An SQLAlchemy model class
        * schema: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, id_: Any, db: Session) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id_ == id_).first()

    def get_all(self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()
    
    def get_multi(self, limit: int, skip: int, db: Session) -> List[ModelType]:
        return db.query(self.model).limit(limit).offset(skip).all()

    def create(self, *, obj_in: CreateSchemaType, db: Session) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)

        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj

    def update(
        self,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
        db: Session
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj

    def delete(self, *, id_: Any, db: Session) -> ModelType:
        obj = db.query(self.model).get(id_)

        db.delete(obj)
        db.commit()

        return obj