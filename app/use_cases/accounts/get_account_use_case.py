from app.use_cases.base_use_case import BaseUseCase

from app.infrastructure.repositories.account_repository import AccountRepository

class GetAccountUseCase(BaseUseCase):
    def __init__(self) -> None:
        super().__init__()
        self.accountRepository = AccountRepository()

    def execute(self, id):
        return self.accountRepository.find_account_by_id(id)