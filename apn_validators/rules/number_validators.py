import re
from collections import defaultdict


class Numeric:
    """check is the string only a numeric value"""

    def __init__(self, message="{field_name} only accept numbers") -> None:
        self.message = message

    def validate(self, value, field_name):
        return (
            self.message.format_map(
                defaultdict(str, field_name=field_name, value=value)
            )
            if not re.match(r"^\d+$", value)
            else None
        )


class GreaterThenOrEqual:
    """
    Validator to check if a value is greater than or equal a specified threshold.

    Attributes:
        threshold (int): The threshold value that the input value must exceed.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        threshold: int,
        message="field {field_name} should be greater then or equal {threshold}",
    ):
        self.threshold = threshold
        self.message = message

    def validate(self, value: int, field_name: str):
        """
        Validate if the given value is greater than the threshold.

        Parameters:
            value (str or int): The value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        try:
            value = int(value)
            if value < self.threshold:
                return self.message.format_map(
                    defaultdict(
                        str,
                        field_name=field_name,
                        value=value,
                        threshold=self.threshold,
                    )
                )
        except ValueError:
            return "field {} should be number and greater then or equal {}".format(
                field_name, self.threshold
            )


class GreaterThen:
    """
    Validator to check if a value is greater than a specified threshold.

    Attributes:
        threshold (int): The threshold value that the input value must exceed.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        threshold: int,
        message="field {field_name} should be greater then {threshold}",
    ):
        self.threshold = threshold
        self.message = message

    def validate(self, value: int, field_name: str):
        """
        Validate if the given value is greater than the threshold.

        Parameters:
            value (str or int): The value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        try:
            value = int(value)
            if value <= self.threshold:
                return self.message.format_map(
                    defaultdict(
                        str,
                        field_name=field_name,
                        value=value,
                        threshold=self.threshold,
                    )
                )
        except ValueError:
            return "field {} should be number and greater then {}".format(
                field_name, self.threshold
            )


class LessThenOrEqual:
    """
    Validator to check if a value is less than or equal a specified threshold.

    Attributes:
        threshold (int): The threshold value that the input value must exceed.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        threshold: int,
        message="field {field_name} should be less then or equal {threshold}",
    ):
        self.threshold = threshold
        self.message = message

    def validate(self, value: int, field_name: str):
        """
        Validate if the given value is less than the threshold.

        Parameters:
            value (str or int): The value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        try:
            value = int(value)
            if value > self.threshold:
                return self.message.format_map(
                    defaultdict(
                        str,
                        field_name=field_name,
                        value=value,
                        threshold=self.threshold,
                    )
                )
        except ValueError:
            return "field {} should be number and less then or equal {}".format(
                field_name, self.threshold
            )


class LessThen:
    """
    Validator to check if a value is less than a specified threshold.

    Attributes:
        threshold (int): The threshold value that the input value must exceed.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        threshold: int,
        message="field {field_name} should be less then {threshold}",
    ):
        self.threshold = threshold
        self.message = message

    def validate(self, value: int, field_name: str):
        """
        Validate if the given value is less than the threshold.

        Parameters:
            value (str or int): The value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        try:
            value = int(value)
            if value >= self.threshold:
                return self.message.format_map(
                    defaultdict(
                        str,
                        field_name=field_name,
                        value=value,
                        threshold=self.threshold,
                    )
                )
        except ValueError:
            return "field {} should be number and less then {}".format(
                field_name, self.threshold
            )


Gte = GreaterThenOrEqual
"""Alias for greater than or equal class"""

Gt = GreaterThen
"""Alias for greater than class"""

Lte = LessThenOrEqual
"""Alias for less than or equal class"""

Lt = LessThen
"""Alias for less than class"""


class Range:
    """
    Validator to check if a value is numeric and contains the specified number of decimal places.

    Attributes:
        min (int): The minimum number of decimal places allowed.
        max (int): The maximum number of decimal places allowed.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        min,
        max,
        message="{field_name} should range from {min} to {max}",
    ):
        self.min = min
        self.max = max
        self.message = message

    def validate(self, value, field_name):
        """
        Validate if the given value is numeric and contains the specified number of decimal places.

        Parameters:
            value (str): The value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        if value is None:
            return None

        pattern = r"^-?\d+(\.\d{{{min},{max}}})?$".format(min=self.min, max=self.max)
        if not re.match(pattern, value):
            return self.message.format_map(
                defaultdict(str, field_name=field_name, min=self.min, max=self.max)
            )
        return None


class DigitsBetween:
    """
    Validator to check if a value has a length between a specified minimum and maximum.

    Attributes:
        min (int): The minimum length that the value must have.
        max (int): The maximum length that the value must have.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        min: int,
        max: int,
        message="{field_name} must have a length between {min} and {max}",
    ):
        self.min = min
        self.max = max
        self.message = message

    def validate(self, value, field_name):
        """
        Validate if the given value has a length between the specified minimum and maximum.

        Parameters:
            value (str): The value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        if value is None:
            return None

        length = len(str(value))
        if length < self.min or length > self.max:
            return self.message.format_map(
                defaultdict(str, field_name=field_name, min=self.min, max=self.max)
            )
        return None