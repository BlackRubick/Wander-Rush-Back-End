from typing import List, Optional
from .entities import User

class UserService:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def create_user(self, name: str, email: str, password: str, profile_picture: Optional[str] = None) -> User:
        user = User(id=self.next_id, name=name, email=email, password=password, profile_picture=profile_picture)
        self.users.append(user)
        self.next_id += 1
        return user

    def get_users(self) -> List[User]:
        return self.users

    def delete_user(self, user_id: int) -> bool:
        for user in self.users:
            if user.id == user_id:
                self.users.remove(user)
                return True
        return False
