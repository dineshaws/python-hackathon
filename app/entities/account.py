from pydantic import BaseModel
from typing import Optional

'''
Class to validate router payload
'''
class Account(BaseModel):
    account_number: int
    name: str
    description: str
