import datetime
from collections import defaultdict


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
        target_date: (datetime.date) the date to compare against
        date_format: (str,optional) the date format to validate the date against (default: %Y-%m-%d)
        message: (str,optional) the error message to return if the validation fails
    """

    def __init__(
        self,
        target_date: datetime.date,
        date_format="%Y-%m-%d",
        message="field {field_name} must be equal to {target_date}",
    ) -> None:
        self.message = message
        self.target_date = (
            target_date.date()
            if isinstance(target_date, datetime.datetime)
            else target_date
        )
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
        target_date: (datetime.date) the date to compare against
        date_format: (str,optional) the date format to validate the date against (default: %Y-%m-%d)
        message: (str,optional) the error message to return if the validation
    """

    def __init__(
        self,
        target_date: datetime.date,
        date_format="%Y-%m-%d",
        message="field {field_name} must be after {target_date}",
    ):
        self.target_date = (
            target_date.date()
            if isinstance(target_date, datetime.datetime)
            else target_date
        )
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
        target_date: (datetime.date) the date to compare against
        date_format: (str,optional) the date format to validate the date against (default: %Y-%m-%d)
        message: (str,optional) the error message to return if the validation
    """

    def __init__(
        self,
        target_date: datetime.date,
        date_format="%Y-%m-%d",
        message="field {field_name} must be before {target_date}",
    ):
        self.target_date = (
            target_date.date()
            if isinstance(target_date, datetime.datetime)
            else target_date
        )
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
