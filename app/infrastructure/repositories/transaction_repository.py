from app.infrastructure.repositories.base_repository import BaseRepository

class TransactionRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(table='account_transactions')

    def create_transaction(self, data):
        statement = ("INSERT INTO account_transactions "
              "(accounts_id, txn_type, amount, txn_number, created_on, version) "
              "VALUES (%(accounts_id)s, %(txn_type)s, %(amount)s, %(txn_number)s, %(created_on)s, %(version)s)")
        # Insert salary information
        last_row_id = self.insert_one(statement, data)
        return last_row_id
    
    def find_transactions(self):
        query = ("SELECT * FROM account_transactions")
        records = self.find_all(query)
        return records