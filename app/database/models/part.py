# Copyright 2023 Marin Pejcin


from typing import List, TYPE_CHECKING
from sqlalchemy import String, Integer, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import UUID
import uuid

from app.database.database import Base
from app.database.models.service import Service
from config.enums import PartsCategoryEnum
from app.database.models.relationships.services_parts import services_parts

if TYPE_CHECKING:
    from app.database.models.service import Service


class Part(Base):
    __tablename__ = "part"

    id_: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    cost: Mapped[int] = mapped_column(Integer)
    interval_months: Mapped[int] = mapped_column(Integer)
    interval_kilometers: Mapped[int] = mapped_column(Integer)
    category: Mapped[PartsCategoryEnum] = mapped_column(Enum(PartsCategoryEnum))

    services: Mapped[List["Service"]] = relationship(
        secondary=services_parts, back_populates="parts"
    )
