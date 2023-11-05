# Copyright 2023 Marin Pejcin


from typing import Optional
from pydantic import BaseModel, UUID4

from config.enums import FineCategoryEnum


class FineBase(BaseModel):
    name: Optional[str] = None
    categoty: Optional[FineCategoryEnum] = None
    cost: Optional[int] = None


class FineCreate(FineBase):
    name: str
    category: FineCategoryEnum
    cost: int


class FineUpdate(FineBase):
    pass


class Fine(FineBase):
    id_: UUID4
    expense_id: UUID4

    class Config:
        from_attributes = True
