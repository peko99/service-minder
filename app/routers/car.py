# Copyright 2023 Marin Pejcin


from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from pydantic import UUID4

from app.crud import crud_car
from dependencies import get_db
from app.schemas.car import Car, CarCreate, CarUpdate


router = APIRouter(prefix="/car", tags=["car"], dependencies=[Depends(get_db)])


@router.post("", response_model=Car)
async def create_car(car_in: CarCreate, db: Session = Depends(get_db)) -> Any:
    created_car = crud_car.create(obj_in=car_in, db=db)
    try:
        pass
    except IntegrityError as _:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail=f"Conflict on creating car.",
        )
    else:
        return created_car


@router.get("", response_model=List[Car])
async def get_cars(db: Session = Depends(get_db)) -> Any:
    return crud_car.get_all(db=db)


@router.get("/id/{id_}", response_model=Car)
async def get_car_by_id(id_: UUID4, db: Session = Depends(get_db)) -> Any:
    car = crud_car.get(id_=id_, db=db)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found!")
    return car


@router.put("/{id_}", response_model=Car)
async def update_car(
    id_: UUID4, car_in: CarUpdate, db: Session = Depends(get_db)
) -> Any:
    car = crud_car.get(id_=id_, db=db)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found!")
    try:
        updated_car = crud_car.update(db_obj=car, obj_in=car_in, db=db)
    except IntegrityError as _:
        raise HTTPException(status_code=409, detail="Car could not be updated!")
    return updated_car


@router.delete("/{id_}", response_model=Car)
async def delete_car(id_: UUID4, db: Session = Depends(get_db)) -> Any:
    car = crud_car.get(id_=id_, db=db)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found!")
    return crud_car.delete(id_=id_, db=db)
