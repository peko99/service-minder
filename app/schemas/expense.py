# Copyright 2023 Marin Pejcin


from typing import Optional
from pydantic import BaseModel, UUID4
from datetime import datetime

from config.enums import ExpenseCategoryEnum


class ExpenseBase(BaseModel):
    category: Optional[ExpenseCategoryEnum] = None
    date: Optional[datetime] = None
    mileage: Optional[int] = None
    total_cost: Optional[int] = None


class ExpenseCreate(ExpenseBase):
    category: ExpenseCategoryEnum
    date: datetime
    mileage: int
    total_cost: int
    car_id: UUID4


class ExpenseUpdate(ExpenseBase):
    pass


class Expense(ExpenseBase):
    id_: UUID4
    car_id: UUID4

    class Config:
        from_attributes = True
