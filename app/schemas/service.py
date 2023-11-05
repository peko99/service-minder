# Copyright 2023 Marin Pejcin


from typing import Optional
from pydantic import BaseModel, UUID4


class ServiceBase(BaseModel):
    name: Optional[str] = None
    labour_cost: Optional[int] = None
    parts_total_cost: Optional[int] = None


class ServiceCreate(ServiceBase):
    name: str
    labour_cost: int
    parts_total_cost: int


class ServiceUpdate(ServiceBase):
    pass


class Service(ServiceBase):
    id_: UUID4
    expense_id: UUID4

    class Config:
        from_attributes = True
