from app.infrastructure.config.enum.controller import get_controller_enum

from app.interfaces.controllers.account_controller import AccountController
from app.interfaces.controllers.transaction_controller import TransactionController
from app.interfaces.controllers.seed_controller import SeedController


class ControllerFactory():
    def __init__(self) -> None:
        pass
    def create(self, type):
        if type == get_controller_enum('AccountController'):
            return AccountController()
        if type == get_controller_enum('TransactionController'):
            return TransactionController()
        if type == get_controller_enum('SeedController'):
            return SeedController()
