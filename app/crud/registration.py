# Copyright 2023 Marin Pejcin


from sqlalchemy.orm import Session
from pydantic import UUID4

from app.crud import CRUDBase
from app.database.models.registration import Registration
from app.schemas.registration import RegistrationCreate, RegistrationUpdate


class CRUDRegistration(CRUDBase[Registration, RegistrationCreate, RegistrationUpdate]):
    pass


crud_registration = CRUDRegistration(Registration)
