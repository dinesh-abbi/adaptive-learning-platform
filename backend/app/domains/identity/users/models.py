from app.shared.database.base_model import BaseModel
from app.shared.database.mixins.timestamp import TimestampMixin
from app.shared.database.mixins.uuid import UUIDMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class User(
    UUIDMixin,
    TimestampMixin,
    BaseModel,
):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )