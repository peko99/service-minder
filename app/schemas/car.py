# Copyright 2023 Marin Pejcin


from typing import Optional
from pydantic import BaseModel, UUID4

from config.enums import FuelTypeEnum


class CarTypeBase(BaseModel):
    license_plate: Optional[str] = None
    make: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    mileage: Optional[int] = None
    fuel_capacity: Optional[int] = None
    fuel_type: Optional[FuelTypeEnum] = None
    power: Optional[int] = None


class CarCreate(CarTypeBase):
    make: str
    model: str
    year: int
    mileage: int
    fuel_capacity: int
    power: int
    user_id: UUID4


class CarUpdate(CarTypeBase):
    pass


class Car(CarTypeBase):
    id_: UUID4
    user_id: UUID4

    class Config:
        from_attributes = True
