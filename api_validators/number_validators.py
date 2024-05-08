import re
from .base_validator import _instance_validator


def numeric(value=None, field_name=None):
    """check is the string only a numeric value"""
    field_name, value = _instance_validator._get_field_and_value(field_name, value)
    pattern = r"^\d+$"
    if not re.match(pattern, value):
        _instance_validator.add_error(field_name, f"{field_name} only accept numbers")
    return


def greater_then_or_equal(threshold: int, value=None, field_name=None):
    """must be greater than or equal to minimum value"""
    field_name, value = _instance_validator._get_field_and_value(field_name, value)
    try:
        value = int(value)
        if value < threshold:
            _instance_validator.add_error(
                field_name,
                f"field {field_name} should be greater then or equal {threshold}",
            )
    except ValueError:
        _instance_validator.add_error(
            field_name,
            f"field {field_name} should be number and greater then or equal {threshold}",
        )
    return


def greater_then(threshold: int, value=None, field_name=None):
    """must be greater than threshold value"""
    field_name, value = _instance_validator._get_field_and_value(field_name, value)
    try:
        value = int(value)
        if value <= threshold:
            _instance_validator.add_error(
                field_name,
                f"field {field_name} should be greater then {threshold}",
            )
    except ValueError:
        _instance_validator.add_error(
            field_name,
            f"field {field_name} should be number and greater then {threshold}",
        )
    return


def less_then_or_equal(threshold: int, value=None, field_name=None):
    """must be less than or equal to threshold value"""
    field_name, value = _instance_validator._get_field_and_value(field_name, value)
    try:
        value = int(value)
        if value > threshold:
            _instance_validator.add_error(
                field_name,
                f"field {field_name} should be less then or equal {threshold}",
            )
    except ValueError:
        _instance_validator.add_error(
            field_name,
            f"field {field_name} should be number and less then or equal {threshold}",
        )
    return


def less_then(threshold: int, value=None, field_name=None):
    """must be less than threshold value"""
    field_name, value = _instance_validator._get_field_and_value(field_name, value)
    try:
        value = int(value)
        if value >= threshold:
            _instance_validator.add_error(
                field_name,
                f"field {field_name} should be less then {threshold}",
            )
    except ValueError:
        _instance_validator.add_error(
            field_name,
            f"field {field_name} should be number and less then {threshold}",
        )
    return


def gte(threshold, value=None, field_name=None):
    """Alias for greater than or equal function"""
    return greater_then_or_equal(threshold, value, field_name)


def gt(threshold, value=None, field_name=None):
    """Alias for greater than function"""
    return greater_then(threshold, value, field_name)


def lte(threshold, value=None, field_name=None):
    """Alias for less than or equal function"""
    return less_then_or_equal(threshold, value, field_name)


def lt(threshold, value=None, field_name=None):
    """Alias for less than function"""
    return less_then(threshold, value, field_name)


def decimal(min=None, max=None, value=None, field_name=None):
    """must be numeric and must contain the specified number of decimal places"""
    field_name, value = _instance_validator._get_field_and_value(field_name, value)


def digits(lenght: int, value=None, field_name=None):
    """must have an exact length of value"""
    field_name, value = _instance_validator._get_field_and_value(field_name, value)


def digits_between(min=None, max=None, value=None, field_name=None):
    """must have an exact length of value"""
    field_name, value = _instance_validator._get_field_and_value(field_name, value)


def min_digits(min: int, value=None, field_name=None):
    """must have a minimum length of value"""
    field_name, value = _instance_validator._get_field_and_value(field_name, value)


def max_digits(max: int, value=None, field_name=None):
    """must have a maximum length of value"""
    field_name, value = _instance_validator._get_field_and_value(field_name, value)
