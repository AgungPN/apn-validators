import datetime
from collections import defaultdict


class IsDate:
    """must be a valid date"""

    def __init__(self, message="{field_name} is not a valid date"):
        self.message = message

    def validate(self, str_format: str, value, field_name):
        try:
            datetime.datetime.strptime(value, str_format)
        except:
            return self.message.format_map(
                defaultdict(str, field_name=field_name, str_format=str_format)
            )


class DateEquals:
    """Validate that the provided date value is equal to the target date."""

    def __init__(
        self, target_date: datetime.date, message="Invalid date format: {value}"
    ) -> None:
        self.message = message
        self.target_date = target_date

    def validate(self, value, field_name):
        try:
            if isinstance(value, datetime.date):
                value = value.strftime("%Y-%m-%d")
            parsed_date = datetime.datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            return "Invalid date format: {}".format(value)

        if parsed_date != self.target_date:
            return self.message.format_map(
                defaultdict(
                    str,
                    field_name=field_name,
                    target_date=self.target_date,
                    value=value,
                )
            )


class DateAfter:
    """Validate that the provided date value is after the target date."""

    def __init__(
        self, target_date, message="{d[field_name]} must be after {d[target_date]}"
    ):
        self.target_date = target_date
        self.message = message

    def validate(self, value, field_name):
        try:
            parsed_date = datetime.datetime.strptime(value, "%Y-%m-%d").date()
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
    """Validate that the provided date value is before the target date."""

    def __init__(
        self, target_date, message="{d[field_name]} must be before {d[target_date]}"
    ):
        self.target_date = target_date
        self.message = message

    def validate(self, value, field_name):
        try:
            parsed_date = datetime.datetime.strptime(value, "%Y-%m-%d").date()
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


class DateFormat:
    """Validate that the provided value matches the specified date format."""

    def __init__(
        self,
        str_format="%Y-%m-%d",
        message="{field_name} does not match the specified date format: {d[str_format]}",
    ):
        self.str_format = str_format
        self.message = message

    def validate(self, value, field_name):
        try:
            datetime.datetime.strptime(value, self.str_format)
        except ValueError:
            return self.message.format_map(
                defaultdict(
                    str,
                    field_name=field_name,
                    value=value,
                )
            )
