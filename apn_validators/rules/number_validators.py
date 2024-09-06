import re
from collections import defaultdict


class Numeric:
    """check if the value is a number"""

    def __init__(self, message="{field_name} only accept numbers") -> None:
        self.message = message

    def validate(self, value, field_name):
        try:
            float(value)
            return None
        except ValueError:
            return self.message.format_map(
                defaultdict(str, field_name=field_name, value=value)
            )


class GreaterThenOrEqual:
    """
    Validator to check if a value is greater than or equal a specified threshold.

    Attributes:
        threshold (float): The threshold value that the input value must exceed.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        threshold: float,
        message="field {field_name} should be number and greater then or equal to {threshold}",
    ):
        self.threshold = threshold
        self.message = message

    def validate(self, value: float, field_name: str):
        """
        Validate if the given value is greater than the threshold.

        Parameters:
            value (str or float): The value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """

        error_message = self.message.format_map(
            defaultdict(
                str,
                field_name=field_name,
                value=value,
                threshold=self.threshold,
            )
        )
        try:
            value = float(value)
            if value < self.threshold:
                return error_message
        except ValueError:
            return error_message


class GreaterThen:
    """
    Validator to check if a value is greater than a specified threshold.

    Attributes:
        threshold (float): The threshold value that the input value must exceed.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        threshold: float,
        message="field {field_name} should be number and greater then {threshold}",
    ):
        self.threshold = threshold
        self.message = message

    def validate(self, value: float, field_name: str):
        """
        Validate if the given value is greater than the threshold.

        Parameters:
            value (str or float): The value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        error_message = self.message.format_map(
            defaultdict(
                str,
                field_name=field_name,
                value=value,
                threshold=self.threshold,
            )
        )
        try:
            value = float(value)
            if value <= self.threshold:
                return error_message
        except ValueError:
            return error_message


class LessThenOrEqual:
    """
    Validator to check if a value is less than or equal a specified threshold.

    Attributes:
        threshold (float): The threshold value that the input value must exceed.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        threshold: float,
        message="field {field_name} should be number and less then or equal to {threshold}",
    ):
        self.threshold = threshold
        self.message = message

    def validate(self, value: float, field_name: str):
        """
        Validate if the given value is less than the threshold.

        Parameters:
            value (str or float): The value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        error_message = self.message.format_map(
            defaultdict(
                str,
                field_name=field_name,
                value=value,
                threshold=self.threshold,
            )
        )
        try:
            value = float(value)
            if value > self.threshold:
                return error_message
        except ValueError:
            return error_message


class LessThen:
    """
    Validator to check if a value is less than a specified threshold.

    Attributes:
        threshold (float): The threshold value that the input value must exceed.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        threshold: float,
        message="field {field_name} must be number and less then {threshold}",
    ):
        self.threshold = threshold
        self.message = message

    def validate(self, value: float, field_name: str):
        """
        Validate if the given value is less than the threshold.

        Parameters:
            value (str or float): The value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        error_message = self.message.format_map(
            defaultdict(
                str,
                field_name=field_name,
                value=value,
                threshold=self.threshold,
            )
        )
        try:
            value = float(value)
            if value >= self.threshold:
                return error_message
        except ValueError:
            return error_message


Gte = GreaterThenOrEqual
"""Alias for greater than or equal class"""

Gt = GreaterThen
"""Alias for greater than class"""

Lte = LessThenOrEqual
"""Alias for less than or equal class"""

Lt = LessThen
"""Alias for less than class"""


class NumberRange:
    """
    Validate to check if a value is has number between min and max

    Attributes:
        min (int|float): The minimum number allowed.
        max (int|float): The maximum number allowed.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        min,
        max,
        message="field {field_name} must be between from {min} and {max}",
    ):
        self.min = min
        self.max = max
        self.message = message

    def validate(self, value, field_name):
        """
        Validate if the given value is numeric and contains the specified number of decimal places.
        """
        error_message = self.message.format_map(
            defaultdict(
                str, field_name=field_name, min=self.min, max=self.max, value=value
            )
        )
        try:
            value = float(value)
            if value < self.min or value > self.max:
                return error_message
        except ValueError:
            return error_message


class DecimalRange:
    """
    Validate to check if a value is has decimal between min and max

    Attributes:
        min (int): The minimum number of decimal places allowed.
        max (int): The maximum number of decimal places allowed.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        min,
        max,
        message="The decimal {field_name} must range from {min} to {max}",
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

        value = str(value)
        pattern = r"^-?\d+(\.\d{{{min},{max}}})?$".format(min=self.min, max=self.max)
        if not re.match(pattern, value):
            return self.message.format_map(
                defaultdict(str, field_name=field_name, min=self.min, max=self.max)
            )
        return None


class DigitsBetween:
    """
    Validator to check if a value has a length between a specified minimum and maximum.
    Check by: if length < min or length > max will return error

    Attributes:
        min (int): The minimum length that the value must have.
        max (int): The maximum length that the value must have.
        decimal_include (bool): Include decimal or not when calculate length (default: True).
        dot_include (bool): Include dot or not when calculate length (default: False).
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        min: int,
        max: int,
        decimal_include: bool = True,
        dot_include: bool = False,
        message="field {field_name} must have a length between {min} and {max}",
    ):
        self.min = min
        self.max = max
        self.dot_include = dot_include
        self.decimal_include = decimal_include
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
        value = str(value)
        if not self.decimal_include:
            value = value.split(".")[0]
        if not self.dot_include:
            value = value.replace(".", "")

        length = len(value)
        if length < self.min or length > self.max:
            return self.message.format_map(
                defaultdict(str, field_name=field_name, min=self.min, max=self.max)
            )
        return None
