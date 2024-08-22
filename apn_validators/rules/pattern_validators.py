import re
from collections import defaultdict


class MatchRegex:
    """
    Validator to check if a value matches a specified regular expression pattern.

    Attributes:
        pattern (str): The regular expression pattern to match against.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        pattern: str,
        message="{field_name} field must match with this pattern {pattern}",
    ):
        self.pattern = pattern
        self.message = message

    def validate(self, value: str, field_name: str):
        """
        Validate that the given value matches the specified regular expression pattern.

        Parameters:
            value (str): The value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        if not re.match(self.pattern, value):
            return self.message.format_map(
                defaultdict(str, field_name=field_name, pattern=self.pattern)
            )
        return None


class NotMatchRegex:
    """
    Validator to check if a value does not match a specified regular expression pattern.

    Attributes:
        pattern (str): The regular expression pattern to check against.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        pattern: str,
        message="{field_name} field must not match with this pattern {pattern}",
    ):
        self.pattern = pattern
        self.message = message

    def validate(self, value: str, field_name: str):
        """
        Validate that the given value does not match the specified regular expression pattern.

        Parameters:
            value (str): The value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        if re.match(self.pattern, value):
            return self.message.format_map(
                defaultdict(str, field_name=field_name, pattern=self.pattern)
            )
        return None


class Password:
    """
    Validate the strength of a password based on various criteria.

    Parameters:
        uppercase (bool, optional): Whether the password must contain uppercase letters (default: True).
        lowercase (bool, optional): Whether the password must contain lowercase letters (default: True).
        numbers (bool, optional): Whether the password must contain numeric digits (default: True).
        symbols (bool, optional): Whether the password must contain symbols (default: True).
        length (int, optional): The minimum length of the password (default: 8).
    """

    def __init__(
        self,
        uppercase: bool = True,
        lowercase: bool = True,
        numbers: bool = True,
        symbols: bool = True,
        length: int = 8,
        messages: dict[str, str] = {
            "base_message": "{field_name} field must include at least {messages}",
            "uppercase": "one uppercase letter",
            "lowercase": "one lowercase letter",
            "numbers": "one digit",
            "symbols": "one symbol",
            "length": "be at least {length} characters",
        },
    ) -> None:
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.numbers = numbers
        self.symbols = symbols
        self.length = length
        self.messages = messages

    def __build_patter_password(self):
        pattern = "^"
        problem_message = []
        if self.uppercase:
            pattern += "(?=.*?[A-Z])"
            problem_message.append(
                self.messages.get("uppercase", "one uppercase letter")
            )
        if self.lowercase:
            pattern += "(?=.*?[a-z])"
            problem_message.append(
                self.messages.get("lowercase", "one lowercase letter")
            )
        if self.numbers:
            pattern += "(?=.*?[0-9])"
            problem_message.append(self.messages.get("numbers", "one digit"))
        if self.symbols:
            pattern += "(?=.*?[#?!@_$%^&*-])"
            problem_message.append(self.messages.get("symbols", "one symbol"))
        if self.length is not None:
            pattern = pattern + ".{" + str(self.length) + ",}"
            problem_message.append(
                self.messages.get(
                    "length", "be at lease {length} characters"
                ).format_map(defaultdict(str, length=self.length))
            )

        pattern += "$"
        return pattern, problem_message

    def validate(self, value, field_name):

        pattern, problem_message = self.__build_patter_password()

        if not re.match(r"{}".format(pattern), value):
            problem_message = ", ".join(problem_message)
            return self.messages.get(
                "base_message", "{field_name} field must include at least {messages}"
            ).format_map(
                defaultdict(str, field_name=field_name, messages=problem_message)
            )
        return None


class Email:
    """
    Validate that a string value is a valid email address.

    Parameters:
        value (str, optional): The string value to validate. If None, it will be retrieved from the data by the setter before validation (default: None).
        field_name (str, optional): The name of the field being validated. If None, it will be retrieved from the data by the setter before validation (default: None).

    Returns:
        None
    """

    def __init__(
        self, message="field {field_name} is not a valid email address"
    ) -> None:
        self.message = message

    def validate(self, value, field_name):
        pattern = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
        if not re.match(pattern, value):
            return self.message.format_map(
                defaultdict(str, field_name=field_name, value=value)
            )


# # TODO
# def url(value=None, field_name=None):
#     field_name, value = _instance_validator._get_field_and_value(field_name, value)
#     add_validated_values(field_name, value)


# # TODO
# def ip(value=None, field_name=None):
#     field_name, value = _instance_validator._get_field_and_value(field_name, value)
#     add_validated_values(field_name, value)
