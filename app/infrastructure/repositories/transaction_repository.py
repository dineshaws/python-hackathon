from app.infrastructure.repositories.base_repository import BaseRepository

class TransactionRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(table='transactions')

    def create_transaction(self, data):
        statement = ("INSERT INTO transactions "
              "(transaction_number, amount, type) "
              "VALUES (%(transaction_number)s, %(amount)s, %(type)s)")
        # Insert salary information
        last_row_id = self.insert_one(statement, data)
        return last_row_id
    
    def find_transactions(self):
        query = ("SELECT * FROM transactions")
        records = self.find_all(query)
        return records