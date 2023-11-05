# Copyright 2023 Marin Pejcin


from sqlalchemy import Table, Column, ForeignKey

from app.database.database import Base


services_parts = Table(
    "services_parts",
    Base.metadata,
    Column("service_id", ForeignKey("service.id_")),
    Column("part_id", ForeignKey("part.id_")),
)
