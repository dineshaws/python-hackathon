from app.use_cases.base_use_case import BaseUseCase
from app.infrastructure.repositories.base_repository import BaseRepository


class DropTablesUseCase(BaseUseCase):
    def __init__(self) -> None:
        super().__init__()
        self.baseRepository = BaseRepository()

    def execute(self):
        return self.baseRepository.drop_tables()