import datetime
from collections import defaultdict


def _handler_to_date(target_date, date_format="%Y-%m-%d"):
    """
    Convert the target date to a datetime.date object
    if it is a string then try to convert it to a datetime.date object using the date_format

    Parameters:
        target_date: (datetime.date, str) the date to convert, you can also use special strings like "today", "yesterday","tomorrow"
        date_format: (str,optional) the date format to validate the date against (default: %Y-%m-%d)

    Return:
        datetime.date: the date object
    """
    if isinstance(target_date, datetime.datetime):
        return target_date.date()
    elif isinstance(target_date, str):
        if target_date == "today":
            return datetime.date.today()
        elif target_date == "yesterday":
            return datetime.date.today() - datetime.timedelta(days=1)
        elif target_date == "tomorrow":
            return datetime.date.today() + datetime.timedelta(days=1)

        return datetime.datetime.strptime(target_date, date_format).date()
    return target_date


class IsDate:
    """
    must be a valid date

    Parameters:
        date_format: (str,optional) the date format to validate the date against (default: %Y-%m-%d)
        message: (str,optional) the error message to return if the validation fails
    """

    def __init__(
        self, date_format="%Y-%m-%d", message="field {field_name} is not a valid date"
    ):
        self.message = message
        self.date_format = date_format

    def validate(self, value, field_name):
        try:
            datetime.datetime.strptime(value, self.date_format)
        except ValueError:
            return self.message.format_map(
                defaultdict(
                    str,
                    field_name=field_name,
                    date_format=self.date_format,
                    value=value,
                )
            )


class DateEquals:
    """
    Validate that the provided date value is equal to the target date.

    Parameters:
        target_date: (datetime.date, str) the date to compare against, you can also use the strings "today", "yesterday", "tomorrow" or date in string with specific format
        date_format: (str,optional) the date format to validate the date against (default: %Y-%m-%d)
        message: (str,optional) the error message to return if the validation fails

    Example:
        DateEquals("2024-12-24") -> the date must be equal to 2024-12-24
        DateEquals("yesterday") -> the date must be equal to the yesterday date
        DateEquals("today") -> the date must be equal to the current date
        DateEquals("tomorrow") -> the date must be equal to the tomorrow
        DateEquals(datetime.datetime.strptime("2024-12-12", "%Y-%m-%d")) -> the date must be equal to "2024-12-12"
        DateEquals(datetime.datetime.strptime("2024/12/12", "%Y/%m/%d"), "%Y/%m/%d") /> the date must be equal to "2024/12/12"
    """

    def __init__(
        self,
        target_date: datetime.date | str,
        date_format="%Y-%m-%d",
        message="field {field_name} must be equal to {target_date}",
    ) -> None:
        self.message = message
        self.target_date = _handler_to_date(target_date, date_format)
        self.date_format = date_format

    def validate(self, value, field_name):
        try:
            if isinstance(value, datetime.date):
                value = value.strftime(self.date_format)
            parsed_date = datetime.datetime.strptime(value, self.date_format).date()
        except ValueError:
            return "Invalid date format: {}".format(value)
        if parsed_date != self.target_date:
            return self.message.format_map(
                defaultdict(
                    str,
                    field_name=field_name,
                    target_date=self.target_date,
                    value=value,
                    date_format=self.date_format,
                )
            )


class DateAfter:
    """
    Validate that the provided date value is after the target date.

    Parameters:
        target_date: (datetime.date, str) the date to compare against, you can also use the strings "today", "yesterday", "tomorrow" or date in string with specific format
        date_format: (str,optional) the date format to validate the date against (default: %Y-%m-%d)
        message: (str,optional) the error message to return if the validation

    Example:
        DateAfter("2024-12-24") -> the date must be after 2024-12-24
        DateAfter("yesterday") -> the date must be after yesterday's date
        DateAfter("today") -> the date must be after today's date
        DateAfter("tomorrow") -> the date must be after tomorrow's date
        DateAfter(datetime.datetime.strptime("2024-12-12", "%Y-%m-%d")) -> the date must be after 2024-12-12
        DateAfter(datetime.datetime.strptime("2024/12/12", "%Y/%m/%d"), "%Y/%m/%d") /> the date must be after 2024/12/12
    """

    def __init__(
        self,
        target_date: datetime.date | str,
        date_format="%Y-%m-%d",
        message="field {field_name} must be after {target_date}",
    ):
        self.target_date = _handler_to_date(target_date, date_format)
        self.date_format = date_format
        self.message = message

    def validate(self, value, field_name):
        try:
            parsed_date = datetime.datetime.strptime(value, self.date_format).date()
        except ValueError:
            return "Invalid date format: {}".format(value)

        if parsed_date <= self.target_date:
            return self.message.format_map(
                defaultdict(
                    str,
                    field_name=field_name,
                    target_date=self.target_date,
                    value=value,
                )
            )


class DateBefore:
    """
    Validate that the provided date value is before the target date.
    Parameters:
        target_date: (datetime.date, str) the date to compare against, you can also use the strings "today", "yesterday", "tomorrow" or date in string with specific format
        date_format: (str,optional) the date format to validate the date against (default: %Y-%m-%d)
        message: (str,optional) the error message to return if the validation

    Example:
        DateBefore("2024-12-24") -> the date must be before 2024-12-24
        DateBefore("yesterday") -> the date must be before yesterday's date
        DateBefore("today") -> the date must be before today's date
        DateBefore("tomorrow") -> the date must be before tomorrow's date
        DateBefore(datetime.datetime.strptime("2024-12-12", "%Y-%m-%d")) -> the date must be before 2024-12-12
        DateBefore(datetime.datetime.strptime("2024/12/12", "%Y/%m/%d"), "%Y/%m/%d") /> the date must be before 2024/12/12
    """

    def __init__(
        self,
        target_date: datetime.date | str,
        date_format="%Y-%m-%d",
        message="field {field_name} must be before {target_date}",
    ):
        self.target_date = _handler_to_date(target_date, date_format)
        self.date_format = date_format
        self.message = message

    def validate(self, value, field_name):
        try:
            parsed_date = datetime.datetime.strptime(value, self.date_format).date()
        except ValueError:
            return "Invalid date format: {}".format(value)

        if parsed_date >= self.target_date:
            return self.message.format_map(
                defaultdict(
                    str,
                    field_name=field_name,
                    target_date=self.target_date,
                    value=value,
                )
            )
