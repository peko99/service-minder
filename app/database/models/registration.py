# Copyright 2023 Marin Pejcin


from typing import TYPE_CHECKING
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import UUID
import uuid

from app.database.database import Base

if TYPE_CHECKING:
    from app.database.models.expense import Expense


class Registration(Base):
    __tablename__ = "registration"

    id_: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True)
    insurance_cost: Mapped[int] = mapped_column(Integer)
    road_tax: Mapped[int] = mapped_column(Integer)
    eco_tax: Mapped[int] = mapped_column(Integer)

    expense_id: Mapped[UUID] = mapped_column(ForeignKey("expense.id_"))

    expense: Mapped["Expense"] = relationship(back_populates="registrations")
