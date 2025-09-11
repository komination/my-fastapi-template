from typing import Optional

from sqlmodel import Session, select

from app.domain.entities.user import User
from app.domain.repositories.user_repository import IUserRepository


class UserRepositorySQL(IUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.session.get(User, user_id)

    def get_by_email(self, email: str) -> Optional[User]:
        stmt = select(User).where(User.email == email)
        return self.session.exec(stmt).first()

    def add(self, user: User) -> User:
        self.session.add(user)
        self.session.flush()
        return user

