import re
from .base_validator import _instance_validator


def length(min, max, value=None, field_name=None):
    """
    Validate that the length of a string value falls within a specified range.

    Parameters:
        min_length (int): The minimum allowed length of the string.
        max_length (int): The maximum allowed length of the string.
        value (str, optional): The string value to validate. If None, it will be retrieved from the data by the setter before validation (default: None).
        field_name (str, optional): The name of the field being validated. If None, it will be retrieved from the data by the setter before validation (default: None).


    Returns:
        None
    """
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    len_value = len(value)
    message = None
    is_failed = len_value < min or len_value > max
    if is_failed:
        message = f"lenght {field_name} should be min {min} and max {max}"
        _instance_validator.add_error(field_name, message)
    return message


def not_blank(value=None, field_name=None):
    """
    Validate that a string value is not blank (empty or contains only whitespace).

    Parameters:
        value (str, optional): The string value to validate. If None, it will be retrieved from the data by the setter before validation (default: None).
        field_name (str, optional): The name of the field being validated. If None, it will be retrieved from the data by the setter before validation (default: None).

    Returns:
        None
    """
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    message = None
    if value is None or not str(value).strip():
        message = f"{field_name} should be not blank"
        _instance_validator.add_error(field_name, message)
    return message


def email(value=None, field_name=None):
    """
    Validate that a string value is a valid email address.

    Parameters:
        value (str, optional): The string value to validate. If None, it will be retrieved from the data by the setter before validation (default: None).
        field_name (str, optional): The name of the field being validated. If None, it will be retrieved from the data by the setter before validation (default: None).

    Returns:
        None
    """
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    message = None
    pattern = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
    if not re.match(pattern, value):
        message = f"field {field_name} is not a valid email address"
        _instance_validator.add_error(field_name, message)
    return message


def in_list(list_data, value=None, field_name=None):
    """
    Validate that a string value is present in a specified list.

    Parameters:
        list_data (list): The list of valid values.
        value (str, optional): The string value to validate. If None, it will be retrieved from the data by the setter before validation (default: None).
        field_name (str, optional): The name of the field being validated. If None, it will be retrieved from the data by the setter before validation (default: None).

    Returns:
        None
    """
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    message = None
    if value not in list_data:
        message = f"field {field_name} should in {list_data}"
        _instance_validator.add_error(field_name, message)
    return message


def not_in_list(list_data, value=None, field_name=None):
    """
    Validate that a string value is not present in a specified list.

    Parameters:
        list_data (list): The list of invalid values.
        value (str, optional): The string value to validate. If None, it will be retrieved from the data by the setter before validation (default: None).
        field_name (str, optional): The name of the field being validated. If None, it will be retrieved from the data by the setter before validation (default: None).

    Returns:
        None
    """
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    message = None
    if value in list_data:
        message = f"field {field_name} should not in {list_data}"
        _instance_validator.add_error(field_name, message)
    return message


def doesn_start_with(list_prefix: list[str], value: str = None, field_name=None):
    """
    Validate that a string value does not start with any of the specified prefixes.

    Parameters:
        list_prefix (list of str): The list of prefixes that the string should not start with.
        value (str, optional): The string value to validate. If None, it will be retrieved from the data by the setter before validation (default: None).
        field_name (str, optional): The name of the field being validated. If None, it will be retrieved from the data by the setter before validation (default: None).

    Returns:
        None
    """
    field_name, value = _instance_validator._get_field_and_value(field_name, value)
    error_message = None
    if value.startswith(list_prefix):
        error_message = f"field {field_name} should not start with in {list_prefix}"
        _instance_validator.add_error(field_name, error_message)
    return error_message


def start_with(list_prefix: tuple[str], value: str = None, field_name=None):
    """
    Validate that a string value starts with one of the specified prefixes.

    Parameters:
        list_prefix (tuple of str): The tuple of prefixes that the string should start with.
        value (str, optional): The string value to validate. If None, it will be retrieved from the data by the setter before validation (default: None).
        field_name (str, optional): The name of the field being validated. If None, it will be retrieved from the data by the setter before validation (default: None).

    Returns:
        None
    """
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    error_message = None
    if not value.startswith(list_prefix):
        error_message = f"field {field_name} should start with in {list_prefix}"
        _instance_validator.add_error(field_name, error_message)
    return error_message


def doesn_end_with(list_tail: tuple[str], value: str = None, field_name=None):
    """
    Validate that a string value does not end with any of the specified suffixes.

    Parameters:
        list_tail (tuple of str): The tuple of suffixes that the string should not end with.
        value (str, optional): The string value to validate. If None, it will be retrieved from the data by the setter before validation (default: None).
        field_name (str, optional): The name of the field being validated. If None, it will be retrieved from the data by the setter before validation (default: None).

    Returns:
        None
    """
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    error_message = None
    if value.endswith(list_tail):
        error_message = f"field {field_name} should end with in {list_tail}"
        _instance_validator.add_error(field_name, error_message)
    return error_message


def end_with(list_tail: list[str], value=None, field_name=None):
    """
    Validate that a string value ends with one of the specified suffixes.

    Parameters:
        list_tail (list of str): The list of suffixes that the string should end with.
        value (str, optional): The string value to validate. If None, it will be retrieved from the data by the setter before validation (default: None).
        field_name (str, optional): The name of the field being validated. If None, it will be retrieved from the data by the setter before validation (default: None).

    Returns:
        None
    """
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    error_message = None
    if not value.endswith(list_tail):
        error_message = f"field {field_name} should end with in {list_tail}"
        _instance_validator.add_error(field_name, error_message)
    return error_message


def equals(another_value, value: str = None, field_name=None):
    """
    Validate that a string value is equal to another specified value.

    Parameters:
        another_value: The value to compare against.
        value (str, optional): The string value to validate. If None, it will be retrieved from the data by the setter before validation (default: None).
        field_name (str, optional): The name of the field being validated. If None, it will be retrieved from the data by the setter before validation (default: None).

    Returns:
        None
    """
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    error_message = None
    if str(value) != str(another_value):
        error_message = f"field {field_name} must same with {another_value}"
    return error_message


def not_equals(another_value, value: str = None, field_name=None):
    """
    Validate that a string value is not equal to another specified value.

    Parameters:
        another_value: The value to compare against.
        value (str, optional): The string value to validate. If None, it will be retrieved from the data by the setter before validation (default: None).
        field_name (str, optional): The name of the field being validated. If None, it will be retrieved from the data by the setter before validation (default: None).

    Returns:
        None
    """
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    error_message = None
    if str(value) == str(another_value):
        error_message = f"field {field_name} must not same with {another_value}"
    return error_message


if __name__ == "__main__":
    print(_instance_validator.get_errors())
    equals("123")
    print(end_with(("Agung", "Prasets"), value="Agung Prasetyo Nugroho"))
