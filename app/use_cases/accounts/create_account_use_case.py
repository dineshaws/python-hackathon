from app.use_cases.base_use_case import BaseUseCase


from app.infrastructure.repositories.account_repository import AccountRepository

class CreateAccountUseCase(BaseUseCase):
    def __init__(self) -> None:
        super().__init__()
        self.accountRepository = AccountRepository()

    def execute(self, data):
        return self.accountRepository.create_account(data)