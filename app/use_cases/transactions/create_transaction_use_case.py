from app.use_cases.base_use_case import BaseUseCase

from app.infrastructure.repositories.transaction_repository import TransactionRepository

class CreateTransactionUseCase(BaseUseCase):
    def __init__(self) -> None:
        super().__init__()
        self.transactionRepository = TransactionRepository()

    def execute(self, data):
        return self.transactionRepository.create_transaction(data)