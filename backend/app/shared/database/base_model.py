from app.db.base import Base


class BaseModel(Base):
    """
    Parent class for all application database models.

    Every SQLAlchemy model in the project should inherit from this class
    instead of inheriting directly from Base.
    """

    __abstract__ = True