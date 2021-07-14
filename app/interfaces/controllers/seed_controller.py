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
                "account_balance": 100,
                "description": "Worked on python module",
                "account_name": "Dinesh Prajapati",
                "version": 0,
            },
            {
                "account_number": 2,
                "account_balance": 200,
                "description": "Worked on angular module",
                "account_name": "Vijay",
                "version": 0,
            },
            {
                "account_number": 3,
                "account_balance": 300,
                "description": "Worked on grails module",
                "account_name": "Hitendra",
                "version": 0,
            }
        ]

        transactions = [
            {
                "accounts_id": 1,
                "amount": 100,
                "txn_type": "Cr",
                "txn_number": "1626220800000",
                "created_on": "2021-07-15T00:00:00.000Z",
                "version": 0,
            },
            {
                "accounts_id": 2,
                "amount": 200,
                "txn_type": "Cr",
                "txn_number": "1626220800000",
                "created_on": "2021-07-15T00:00:00.000Z",
                "version": 0,
            },
            {
                "accounts_id": 3,
                "amount": 300,
                "txn_type": "Cr",
                "txn_number": "1626220800000",
                "created_on": "2021-07-15T00:00:00.000Z",
                "version": 0,
            }
        ]

        for account in accounts:
            CreateAccountUseCase().execute(account)
        
        for transaction in transactions:
            CreateTransactionUseCase().execute(transaction)
        return True