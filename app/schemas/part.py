# Copyright 2023 Marin Pejcin


from typing import Optional
from pydantic import BaseModel, UUID4

from config.enums import PartsCategoryEnum


class PartBase(BaseModel):
    name: Optional[str] = None
    cost: Optional[int] = None
    interval_months: Optional[int] = None
    interval_kilometers: Optional[int] = None
    categoty: Optional[PartsCategoryEnum] = None


class PartCreate(PartBase):
    name: str
    cost: int
    interval_months: int
    interval_kilometers: int
    categoty: PartsCategoryEnum


class PartUpdate(PartBase):
    pass


class Part(PartBase):
    id_: UUID4

    class Config:
        from_attributes = True
