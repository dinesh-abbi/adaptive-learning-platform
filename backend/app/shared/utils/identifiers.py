import uuid


def generate_uuid() -> uuid.UUID:
    """
    Generate a UUID for primary keys.

    This function centralizes identifier generation so the
    implementation can evolve (UUIDv7, ULID, etc.) without
    changing every model.
    """
    return uuid.uuid4()