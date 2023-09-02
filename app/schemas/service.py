# Copyright 2023 Marin Pejcin


from typing import Optional
from pydantic import BaseModel, UUID4


class ServiceBase(BaseModel):
    description: Optional[str] = None


class ServiceCreate(ServiceBase):
    description: str


class ServiceUpdate(ServiceBase):
    pass


class Service(ServiceBase):
    id_: UUID4
    description: str

    class Config:
        orm_mode = True
