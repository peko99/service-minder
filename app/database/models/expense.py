# Copyright 2023 Marin Pejcin


from typing import TYPE_CHECKING, List
from datetime import datetime
from sqlalchemy import Integer, Enum, DateTime, ForeignKey
from sqlalchemy.types import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid

from app.database.database import Base
from config.enums import ExpenseCategoryEnum

if TYPE_CHECKING:
    from app.database.models.car import Car
    from app.database.models.service import Service
    from app.database.models.registration import Registration
    from app.database.models.fine import Fine
    from app.database.models.reminder import Reminder


class Expense(Base):
    __tablename__ = "expense"

    id_: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    category: Mapped[ExpenseCategoryEnum] = mapped_column(
        Enum(ExpenseCategoryEnum), nullable=False
    )
    date: Mapped[datetime] = mapped_column(DateTime)
    mileage: Mapped[int] = mapped_column(Integer)
    total_cost: Mapped[int] = mapped_column(Integer)

    car_id: Mapped[UUID] = mapped_column(ForeignKey("car.id_"))

    car: Mapped["Car"] = relationship(back_populates="expenses")
    services: Mapped[List["Service"]] = relationship(back_populates="expense")
    registrations: Mapped[List["Registration"]] = relationship(back_populates="expense")
    fines: Mapped[List["Fine"]] = relationship(back_populates="expense")
    reminders: Mapped[List["Reminder"]] = relationship(back_populates="expense")
