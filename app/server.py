from fastapi import FastAPI

from app.interfaces.controllers.controller_factory import ControllerFactory
from app.infrastructure.config.enum.controller import get_controller_enum
from app.entities.account import Account
from app.entities.transaction import Transaction

app = FastAPI()


account_controller = ControllerFactory().create(get_controller_enum('AccountController'))
transaction_controller = ControllerFactory().create(get_controller_enum('TransactionController'))
seed_controller = ControllerFactory().create(get_controller_enum('SeedController'))

@app.get('/', status_code=200)
def get_root():
    return {'Foo': 'BAR'}

@app.get('/api/v1/accounts', status_code= 200)
def get_accounts():
    return account_controller.get_all()

@app.get('/api/v1/accounts/{account_id}', status_code= 200)
def get_account(account_id: int):
    return account_controller.get(account_id)

@app.post('/api/v1/accounts', status_code=201)
def create_account(account: Account):
    account_dict = account.__dict__ # create dictionary of class object
    last_row_id = account_controller.create(account_dict)
    account_dict['id'] = last_row_id
    return account_dict

@app.put('api/v1/accounts/{account_id}', status_code= 200)
def edit_account(account_id: int, account: Account):
    return account

@app.post('/api/v1/transactions', status_code= 201)
def create_transaction(transaction: Transaction):
    transaction_dict = transaction.__dict__
    print("🚀 ~ file: server.py ~ line 40 ~ transaction_dict", transaction_dict)
    last_row_id = transaction_controller.create_transaction(transaction_dict)
    transaction_dict['id'] = last_row_id
    return transaction_dict

@app.get('/api/v1/transactions', status_code= 200)
def get_transactions():
    return transaction_controller.get_transactions()

@app.post('/api/v1/seed-data', status_code= 200)
def seed_data():
    seed_controller.import_data()
    return {'message': 'success'}