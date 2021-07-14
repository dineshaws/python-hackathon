from pydantic import BaseModel
from typing import Optional
# importing enum for enumerations
'''
transaction schema
'''
class Transaction(BaseModel):
    accounts_id: int
    amount: int
    txn_type: str
    txn_number: str
    created_on: str