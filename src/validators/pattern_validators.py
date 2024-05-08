import re
from .base_validator import _instance_validator


def match_regex(pattern: str, value: str = None, field_name=None):
    """
    Validate that a value matches a specified regular expression pattern.

    Parameters:
        pattern (str): The regular expression pattern to match against.
        value (str, optional): The value to validate. If None, the value will be retrieved from the data by setter before validation (default: None).
        field_name (str, optional): The name of the field being validated. If None, the value will be retrieved from the data by setter before validation (default: None).

    Returns:
        None or error message
    """
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    error_message = None
    if not re.match(rf"{pattern}", value):
        error_message = (f"{field_name} field must match with this pattern {pattern}",)
        _instance_validator.add_error(field_name, error_message)
    return error_message


def not_match_regex(pattern: str, value: str = None, field_name=None):
    """
    Validate that a value does not match a specified regular expression pattern.

    Parameters:
        pattern (str): The regular expression pattern to check against.
        value (str, optional): The value to validate. If None, it will be retrieved from the data by the setter before validation (default: None).
        field_name (str, optional): The name of the field being validated. If None, it will be retrieved from the data by the setter before validation (default: None).

    Returns:
        None or error message
    """
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    error_message = None
    if re.match(rf"{pattern}", value):
        error_message = (
            f"{field_name} field must not match with this pattern {pattern}",
        )
        _instance_validator.add_error(field_name, error_message)
    return error_message


def __build_patter_password(uppercase, lowercase, numbers, symbols, length):
    pattern = "^"
    problem_message = []
    if uppercase:
        pattern += "(?=.*?[A-Z])"
        problem_message.append("one uppercase letter")
    if lowercase:
        pattern += "(?=.*?[a-z])"
        problem_message.append("one lowercase letter")
    if numbers:
        pattern += "(?=.*?[0-9])"
        problem_message.append("one digit")
    if symbols:
        pattern += "(?=.*?[#?!@_$%^&*-])"
        problem_message.append("one symbol")
    if length is not None:
        pattern = pattern + ".{" + str(length) + ",}"
        problem_message.append(f"be at least {length} characters")

    pattern += "$"
    return pattern, problem_message


def password(
    uppercase: bool = True,
    lowercase: bool = True,
    numbers: bool = True,
    symbols: bool = True,
    length: int = 8,
    value=None,
    field_name=None,
):
    """
    Validate the strength of a password based on various criteria.

    Parameters:
        uppercase (bool, optional): Whether the password must contain uppercase letters (default: True).
        lowercase (bool, optional): Whether the password must contain lowercase letters (default: True).
        numbers (bool, optional): Whether the password must contain numeric digits (default: True).
        symbols (bool, optional): Whether the password must contain symbols (default: True).
        length (int, optional): The minimum length of the password (default: 8).
        value (str, optional): The value to validate. If None, it will be retrieved from the data by the setter before validation (default: None).
        field_name (str, optional): The name of the field being validated. If None, it will be retrieved from the data by the setter before validation (default: None).

    Returns:
        None or error message
    """
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    pattern, problem_message = __build_patter_password(
        uppercase, lowercase, numbers, symbols, length
    )

    error_message = None
    if not re.match(rf"{pattern}", value):
        problem_message = ", ".join(problem_message)
        error_message = (f"{field_name} field must include at least {problem_message}",)
        _instance_validator.add_error(field_name, error_message)
    return error_message


# TODO
def url(value=None, field_name=None):
    field_name, value = _instance_validator._get_field_and_value(field_name, value)


# TODO
def ip(value=None, field_name=None):
    field_name, value = _instance_validator._get_field_and_value(field_name, value)
