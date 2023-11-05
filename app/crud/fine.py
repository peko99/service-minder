# Copyright 2023 Marin Pejcin


from sqlalchemy.orm import Session
from pydantic import UUID4

from app.crud import CRUDBase
from app.database.models.fine import Fine
from app.schemas.fine import FineCreate, FineUpdate


class CRUDFine(CRUDBase[Fine, FineCreate, FineUpdate]):
    pass


crud_fine = CRUDFine(Fine)
