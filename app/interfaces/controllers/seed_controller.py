from app.interfaces.controllers.base_controller import BaseController
from app.use_cases.drop_tables_use_case import DropTablesUseCase
from app.use_cases.create_tables_use_case import CreateTablesUseCase
from app.use_cases.accounts.create_account_use_case import CreateAccountUseCase
from app.use_cases.transactions.create_transaction_use_case import CreateTransactionUseCase

class SeedController(BaseController):
    def __init__(self) -> None:
        super().__init__()

    def import_data(self):
        DropTablesUseCase().execute()
        CreateTablesUseCase().execute()
        accounts = [
            {
                "account_number": 1,
                "name": "dinesh",
                "description": "Working on python module"
            },
            {
                "account_number": 2,
                "name": "vijay",
                "description": "Working on angular module"
            },
            {
                "account_number": 3,
                "name": "hitendra",
                "description": "Working on grails module"
            }
        ]

        transactions = [
            {
                "transaction_number": 101,
                "amount": 100,
                "type": "Dr"
            },
            {
                "transaction_number": 102,
                "amount": 200,
                "type": "Cr"
            }
        ]

        for account in accounts:
            CreateAccountUseCase().execute(account)
        
        for transaction in transactions:
            CreateTransactionUseCase().execute(transaction)
        return True