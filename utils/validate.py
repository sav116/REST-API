import uuid


def is_valid_uuid(*values):
    for value in values:
        try:
            uuid.UUID(value)
        except ValueError:
            return False
    return True
