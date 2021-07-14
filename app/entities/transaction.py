from pydantic import BaseModel
from typing import Optional
# importing enum for enumerations
'''
transaction schema
'''
class Transaction(BaseModel):
    transaction_number: int
    amount: int
    type: str