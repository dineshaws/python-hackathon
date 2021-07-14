from app.interfaces.controllers.base_controller import BaseController

from app.use_cases.transactions.create_transaction_use_case import CreateTransactionUseCase
from app.use_cases.transactions.get_transactions_use_case import GetTransactionsUseCase

class TransactionController(BaseController):
    def __init__(self) -> None:
        super().__init__()
    
    def create_transaction(self, data):
        return CreateTransactionUseCase().execute(data)
    
    def get_transactions(self):
        return GetTransactionsUseCase().execute()