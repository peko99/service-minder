# Copyright 2023 Marin Pejcin


from sqlalchemy.orm import Session
from pydantic import UUID4

from app.crud import CRUDBase
from app.database.models.part import Part
from app.schemas.part import PartCreate, PartUpdate


class CRUDPart(CRUDBase[Part, PartCreate, PartUpdate]):
    pass


crud_part = CRUDPart(Part)
