# Copyright 2023 Marin Pejcin


from typing import Optional
from pydantic import BaseModel, UUID4


class ReminderBase(BaseModel):
    name: Optional[str] = None
    cost: Optional[int] = None
    interval_months: Optional[int] = None
    interval_kilometers: Optional[int] = None


class ReminderCreate(ReminderBase):
    name: str
    cost: int
    interval_months: int
    interval_kilometers: int


class ReminderUpdate(ReminderBase):
    pass


class Reminder(ReminderBase):
    id_: UUID4
    expense_id: UUID4

    class Config:
        from_attributes = True
