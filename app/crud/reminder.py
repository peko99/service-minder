# Copyright 2023 Marin Pejcin


from sqlalchemy.orm import Session
from pydantic import UUID4

from app.crud import CRUDBase
from app.database.models.reminder import Reminder
from app.schemas.reminder import ReminderCreate, ReminderUpdate


class CRUDReminder(CRUDBase[Reminder, ReminderCreate, ReminderUpdate]):
    pass


crud_reminder = CRUDReminder(Reminder)