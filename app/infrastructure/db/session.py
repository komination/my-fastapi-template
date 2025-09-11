from contextlib import contextmanager
from typing import Iterator

from sqlmodel import Session, SQLModel, create_engine

from app.core.config import Settings


settings = Settings()
engine = create_engine(settings.DATABASE_URL, echo=False, pool_pre_ping=True)


def init_db() -> None:
    # For development only; in production use Alembic migrations
    SQLModel.metadata.create_all(bind=engine)


@contextmanager
def session_scope() -> Iterator[Session]:
    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

