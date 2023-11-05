# Copyright 2023 Marin Pejcin


from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from pydantic import UUID4

from app.crud import crud_service
from dependencies import get_db
from app.schemas.service import Service, ServiceCreate, ServiceUpdate


router = APIRouter(prefix="/service", tags=["service"], dependencies=[Depends(get_db)])


@router.post("", response_model=Service)
async def create_service(
    service_in: ServiceCreate, db: Session = Depends(get_db)
) -> Any:
    try:
        created_service = crud_service.create(obj_in=service_in, db=db)
    except IntegrityError as _:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail=f"Conflict on creating service.",
        )
    else:
        return created_service


@router.get("", response_model=List[Service])
async def get_services(db: Session = Depends(get_db)) -> Any:
    return crud_service.get_all(db=db)


@router.get("/id/{id_}", response_model=Service)
async def get_service_by_id(id_: UUID4, db: Session = Depends(get_db)) -> Any:
    service = crud_service.get(id_=id_, db=db)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found!")
    return service


@router.put("/{id_}", response_model=Service)
async def update_service(
    id_: UUID4, service_in: ServiceUpdate, db: Session = Depends(get_db)
) -> Any:
    service = crud_service.get(id_=id_, db=db)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found!")
    try:
        updated_service = crud_service.update(db_obj=service, obj_in=service_in, db=db)
    except IntegrityError as _:
        raise HTTPException(status_code=409, detail="Service could not be updated!")
    return updated_service


@router.delete("/{id_}", response_model=Service)
async def delete_service(id_: UUID4, db: Session = Depends(get_db)) -> Any:
    service = crud_service.get(id_=id_, db=db)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found!")
    return crud_service.delete(id_=id_, db=db)
