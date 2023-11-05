# Copyright 2023 Marin Pejcin


from typing import TYPE_CHECKING, List
from sqlalchemy import String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.types import UUID
import uuid

from app.database.database import Base
from config.enums import FuelTypeEnum

if TYPE_CHECKING:
    from app.database.models.user import User
    from app.database.models.expense import Expense


class Car(Base):
    __tablename__ = "car"

    id_: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    license_plate: Mapped[str] = mapped_column(String, nullable=False)
    make: Mapped[str] = mapped_column(String)
    model: Mapped[str] = mapped_column(String)
    year: Mapped[int] = mapped_column(Integer)
    mileage: Mapped[int] = mapped_column(Integer)
    fuel_capacity: Mapped[int] = mapped_column(Integer)
    fuel_type: Mapped[FuelTypeEnum] = mapped_column(Enum(FuelTypeEnum), nullable=False)
    power: Mapped[int] = mapped_column(Integer)

    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id_"))

    user: Mapped["User"] = relationship(back_populates="cars")
    expenses: Mapped[List["Expense"]] = relationship(back_populates="car")
