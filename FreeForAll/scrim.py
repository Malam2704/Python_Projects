def password_validator(password: str) -> bool:
    """Validate a password based on specific criteria.

    The password must:
    - Be at least 8 characters long
    - Contain at least one uppercase letter
    - Contain at least one lowercase letter
    - Contain at least one digit
    - Contain at least one special character from the set !@#$%^&*()-_

    Args:
        password (str): The password to validate."""
    special_characters = "!@#$%^&*()-_"
    if(len(password) < 8):
        return False
    if(not any(char.isupper() for char in password)):
        return False
    if(not any(char.islower() for char in password)):
        return False
    if(not any(char.isdigit() for char in password)):
        return False    