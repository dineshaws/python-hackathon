from app.infrastructure.repositories.base_repository import BaseRepository


class AccountRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(table='accounts')

    def find_account_by_id(self, id):
        query = ("SELECT * FROM accounts")
        # Insert salary information
        # data = (1)
        record = self.find_one(query)
        if record:
            return record
        else:
            raise Exception('Account not found')

    def find_accounts(self):
        query = ("SELECT * FROM accounts")
        records = self.find_all(query)
        return records
    
    def create_account(self, data):
        statement = ("INSERT INTO accounts "
              "(account_number, account_balance, description, account_name, version) "
              "VALUES (%(account_number)s, %(account_balance)s, %(description)s, %(account_name)s, %(version)s)")
        # Insert salary information
        last_row_id = self.insert_one(statement, data)
        return last_row_id