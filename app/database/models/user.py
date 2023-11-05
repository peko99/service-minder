# Copyright 2023 Marin Pejcin


from typing import TYPE_CHECKING, List
from sqlalchemy import Boolean, String
from sqlalchemy.types import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
import uuid

from app.database.database import Base

if TYPE_CHECKING:
    from app.database.models.car import Car


class User(Base):
    __tablename__ = "user"

    id_: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    full_name: Mapped[str] = mapped_column(String(55), index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)

    cars: Mapped[List["Car"]] = relationship(back_populates="user")
