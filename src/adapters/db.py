from ..ports.repository import UserRepository
from ..core.entities import User

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}

    def save(self, user: User):
        self.users[user.user_id] = user

    def find_by_id(self, user_id: int) -> User:
        return self.users.get(user_id)
