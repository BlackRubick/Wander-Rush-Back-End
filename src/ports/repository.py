from abc import ABC, abstractmethod
from ..core.entities import User

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User):
        pass

    @abstractmethod
    def find_by_id(self, user_id: int) -> User:
        pass
