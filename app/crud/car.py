# Copyright 2023 Marin Pejcin


from sqlalchemy.orm import Session
from pydantic import UUID4

from app.crud import CRUDBase
from app.database.models.car import Car
from app.schemas.car import CarCreate, CarUpdate


class CRUDCar(CRUDBase[Car, CarCreate, CarUpdate]):
    pass


crud_car = CRUDCar(Car)
