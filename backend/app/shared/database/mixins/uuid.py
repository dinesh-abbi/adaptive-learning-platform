import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.shared.utils.identifiers import generate_uuid


class UUIDMixin:
    """
    Provides a UUID primary key for all database models.
    """

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=generate_uuid,
    )
