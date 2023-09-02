# Copyright 2023 Marin Pejcin


from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database.database import Base


class Service(Base):
    __tablename__ = "service"

    id_ = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    description = Column(String)
    