# Copyright 2023 Marin Pejcin


from typing import TYPE_CHECKING
from sqlalchemy import String, Integer, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import UUID
import uuid

from app.database.database import Base

if TYPE_CHECKING:
    from app.database.models.expense import Expense


class Reminder(Base):
    __tablename__ = "reminder"

    id_: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    interval_months: Mapped[int] = mapped_column(Integer)
    interval_kilometers: Mapped[int] = mapped_column(Integer)

    expense_id: Mapped[UUID] = mapped_column(ForeignKey("expense.id_"))

    expense: Mapped["Expense"] = relationship(back_populates="reminders")
