from .base_validator import _instance_validator
import datetime


def is_date(str_format: str = "%Y-%m-%d", value=None, field_name=None):
    """must be a valid date"""
    field_name, value = _instance_validator._get_field_and_value(field_name, value)
    try:
        datetime.datetime.strptime(value, str_format)
    except:
        error_message = f"{field_name} is not a valid date"
        _instance_validator.add_error(field_name, error_message)
        return error_message


def date_equals(target_date: datetime.date, value=None, field_name=None):
    """Validate that the provided date value is equal to the target date."""
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    try:
        if isinstance(value, datetime.date):
            value = value.strftime("%Y-%m-%d")
        parsed_date = datetime.datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        error_message = f"Invalid date format: {value}"
        _instance_validator.add_error(field_name, error_message)
        return error_message

    if parsed_date != target_date:
        error_message = f"{field_name} does not equal {target_date}"
        _instance_validator.add_error(field_name, error_message)
        return error_message


def date_after(target_date: datetime.date, value=None, field_name=None):
    """Validate that the provided date value is after the target date."""
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    try:
        parsed_date = datetime.datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        error_message = f"Invalid date format: {value}"
        _instance_validator.add_error(field_name, error_message)
        return error_message

    if parsed_date <= target_date:
        error_message = f"{field_name} must be after {target_date}"
        _instance_validator.add_error(field_name, error_message)
        return error_message


def date_before(target_date: datetime.date, value=None, field_name=None):
    """Validate that the provided date value is before the target date."""
    field_name, value = _instance_validator._get_field_and_value(field_name, value)

    try:
        parsed_date = datetime.datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        error_message = f"Invalid date format: {value}"
        _instance_validator.add_error(field_name, error_message)
        return error_message

    if parsed_date >= target_date:
        error_message = f"{field_name} must be before {target_date}"
        _instance_validator.add_error(field_name, error_message)
        return error_message


def date_format(str_format: str = "%Y-%m-%d", value=None, field_name=None):
    """date must a valid date by string format"""
    field_name, value = _instance_validator._get_field_and_value(field_name, value)
    try:
        datetime.datetime.strptime(value, str_format)
    except:
        error_message = (
            f"{field_name} does not match the specified date format: {str_format}"
        )
        _instance_validator.add_error(field_name, error_message)
        return error_message


if __name__ == "__main__":

    current_datetime = datetime.datetime.now()

    # Create two datetime objects with the same date but different times
    target_datetime = current_datetime.replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    value_datetime = current_datetime.replace(
        hour=12, minute=0, second=0, microsecond=0
    )

    print(value_datetime)
    print(target_datetime)
    # Call date_equals with the date components of the datetime objects
    print(date_equals(target_date=target_datetime.date(), value=value_datetime.date()))
