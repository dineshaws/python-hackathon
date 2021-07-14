from pydantic import BaseModel
from typing import Optional

'''
Class to validate router payload
'''
class Account(BaseModel):
    account_number: int
    account_balance: int
    account_name: str
    description: str
