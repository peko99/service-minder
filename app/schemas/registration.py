# Copyright 2023 Marin Pejcin


from typing import Optional
from pydantic import BaseModel, UUID4


class RegistrationBase(BaseModel):
    insurance_cost: Optional[int] = None
    road_tax: Optional[int] = None
    eco_tax: Optional[int] = None


class RegistrationCreate(RegistrationBase):
    name: str
    insurance_cost: int
    road_tax: int
    eco_tax: int


class RegistrationUpdate(RegistrationBase):
    pass


class Registration(RegistrationBase):
    id_: UUID4
    expense_id: UUID4

    class Config:
        from_attributes = True
