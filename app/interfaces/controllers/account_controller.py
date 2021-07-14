from app.interfaces.controllers.base_controller import BaseController

from app.use_cases.accounts.create_account_use_case import CreateAccountUseCase
from app.use_cases.accounts.get_account_use_case import GetAccountUseCase
from app.use_cases.accounts.get_all_accounts_use_case import GetAllAccountsUseCase

class AccountController(BaseController):
    def __init__(self) -> None:
        super().__init__()

    def create(self, data):
        return CreateAccountUseCase().execute(data)

    def get(self, id):
        return GetAccountUseCase().execute(id)
    
    def get_all(self):
        return GetAllAccountsUseCase().execute()