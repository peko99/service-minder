# Copyright 2023 Marin Pejcin


from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database.database import Base


class User(Base):
    __tablename__ = "user"

    id_ = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
