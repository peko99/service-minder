# Copyright 2023 Marin Pejcin


from typing import List, TYPE_CHECKING
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import UUID
import uuid

from app.database.database import Base
from app.database.models.relationships.services_parts import services_parts

if TYPE_CHECKING:
    from app.database.models.expense import Expense
    from app.database.models.part import Part


class Service(Base):
    __tablename__ = "service"

    id_: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    labour_cost: Mapped[int] = mapped_column(Integer)
    parts_total_cost: Mapped[int] = mapped_column(Integer)

    expense_id: Mapped[UUID] = mapped_column(ForeignKey("expense.id_"))

    expense: Mapped["Expense"] = relationship(back_populates="services")
    parts: Mapped[List["Part"]] = relationship(
        secondary=services_parts, back_populates="services"
    )
