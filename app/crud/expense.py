# Copyright 2023 Marin Pejcin


from sqlalchemy.orm import Session
from pydantic import UUID4

from app.crud import CRUDBase
from app.database.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseUpdate


class CRUDExpense(CRUDBase[Expense, ExpenseCreate, ExpenseUpdate]):
    pass


crud_expense = CRUDExpense(Expense)
