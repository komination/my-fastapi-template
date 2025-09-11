from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.user import User


class IUserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        ...

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        ...

    @abstractmethod
    def add(self, user: User) -> User:
        ...

