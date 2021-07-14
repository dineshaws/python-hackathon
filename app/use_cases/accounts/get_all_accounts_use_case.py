from app.infrastructure.repositories.account_repository import AccountRepository

from app.use_cases.base_use_case import BaseUseCase

class GetAllAccountsUseCase(BaseUseCase):
    def __init__(self) -> None:
        super().__init__()
        self.accountRepository = AccountRepository()

    def execute(self):
        return self.accountRepository.find_accounts()