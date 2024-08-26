from collections import defaultdict


class Length:
    """
    Validator to check if the length of a string value falls within a specified range.

    Attributes:
        min_length (int): The minimum allowed length of the string.
        max_length (int): The maximum allowed length of the string.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        min: int,
        max: int,
        message="field {field_name} length must be between {min} and {max}",
    ):
        self.min_length = min
        self.max_length = max
        self.message = message

    def validate(self, value: str, field_name: str):
        """
        Validate that the length of the given string value falls within the specified range.

        Parameters:
            value (str): The string value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        len_value = len(str(value))
        if len_value < self.min_length or len_value > self.max_length:
            return self.message.format_map(
                defaultdict(
                    str, field_name=field_name, min=self.min_length, max=self.max_length
                )
            )
        return None


class MinLength:
    """
    Validator to check if a value has a minimum length.

    Attributes:
        min (int): The minimum length that the value must have.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self, min: int, message="field {field_name} must have a minimum length of {min}"
    ):
        self.min = min
        self.message = message

    def validate(self, value, field_name):
        """
        Validate if the given value has a minimum length.

        Parameters:
            value (str): The value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        if value is None:
            return None

        length = len(str(value))
        if length < self.min:
            return self.message.format_map(
                defaultdict(str, field_name=field_name, min=self.min)
            )
        return None


class MaxLength:
    """
    Validator to check if a value has a maximum length.

    Attributes:
        max (int): The maximum length that the value must have.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self, max: int, message="field {field_name} must have a maximum length of {max}"
    ):
        self.max = max
        self.message = message

    def validate(self, value, field_name):
        """
        Validate if the given value has a maximum length.

        Parameters:
            value (str): The value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        if value is None:
            return None

        length = len(str(value))
        if length > self.max:
            return self.message.format_map(
                defaultdict(str, field_name=field_name, max=self.max)
            )
        return None


class NotBlank:
    """
    Validator to check if a string value is not blank (empty or contains only whitespace).

    Attributes:
        message (str): The error message to be used if the validation fails.
    """

    def __init__(self, message="field {field_name} must not be blank"):
        self.message = message

    def validate(self, value: str, field_name: str):
        """
        Validate that the given string value is not blank.

        Parameters:
            value (str): The string value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        if value is None or not str(value).strip():
            return self.message.format_map(defaultdict(str, field_name=field_name))
        return None


class InList:
    """
    Validator to check if a string value is present in a specified list.

    Attributes:
        valid_values (list): The list of valid values.
        message (str): The error message to be used if the validation fails.
    """

    def __init__(
        self,
        data: list,
        message="field {field_name} must be in {data}",
    ):
        self.data = list(map(str, data))
        self.message = message

    def validate(self, value: str, field_name: str):
        """
        Validate that the given string value is present in the specified list.

        Parameters:
            value (str): The string value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        value = str(value)
        if value not in self.data:
            return self.message.format_map(
                defaultdict(str, field_name=field_name, data=self.data)
            )
        return None


class NotInList:
    """
    Validate that a string value is not present in a specified list.

    Attributes:
        list_data (list): The list of invalid values.
        message (str): The error message template if validation fails.
    """

    def __init__(self, data: list, message="field {field_name} must not be in {data}"):
        self.data = data
        self.message = message

    def validate(self, value: str, field_name: str):
        """
        Validate that the given value is not in the list of invalid values.

        Parameters:
            value (str): The string value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        if value in self.data:
            return self.message.format_map(
                defaultdict(str, field_name=field_name, data=self.data)
            )
        return None


class DoesntStartWith:
    """
    Validate that a string value does not start with any of the specified prefixes.

    Attributes:
        list_prefix (list of str): The list of prefixes that the string should not start with.
        message (str): The error message template if validation fails.
    """

    def __init__(
        self,
        list_prefix: list[str],
        message="field {field_name} must not be start with {list_prefix}",
    ):
        self.list_prefix = list_prefix
        self.message = message

    def validate(self, value: str, field_name: str):
        """
        Validate that the given value does not start with any of the specified prefixes.

        Parameters:
            value (str): The string value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        value = str(value)
        if isinstance(self.list_prefix, tuple):
            list_prefix = tuple(map(str, self.list_prefix))
        else:
            list_prefix = str(self.list_prefix)
        if value.startswith(list_prefix):
            return self.message.format_map(
                defaultdict(str, field_name=field_name, list_prefix=self.list_prefix)
            )
        return None


class StartWith:
    """
    Validate that a string value starts with one of the specified prefixes.

    Attributes:
        list_prefix (tuple of str): The tuple of prefixes that the string should start with.
        message (str): The error message template if validation fails.
    """

    def __init__(
        self,
        list_prefix: tuple[str],
        message="field {field_name} must be start with {list_prefix}",
    ):
        self.list_prefix = list_prefix
        self.message = message

    def validate(self, value: str, field_name: str):
        """
        Validate that the given value starts with one of the specified prefixes.

        Parameters:
            value (str): The string value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        value = str(value)
        if isinstance(self.list_prefix, tuple):
            list_prefix = tuple(map(str, self.list_prefix))
        else:
            list_prefix = str(self.list_prefix)
        if not value.startswith(list_prefix):
            return self.message.format_map(
                defaultdict(str, field_name=field_name, list_prefix=self.list_prefix)
            )
        return None


class DoesntEndWith:
    """
    Validate that a string value does not end with any of the specified suffixes.

    Attributes:
        list_tail (tuple of str): The tuple of suffixes that the string should not end with.
        message (str): The error message template if validation fails.
    """

    def __init__(
        self,
        list_tail: tuple[str],
        message="field {field_name} must not be end with {list_tail}",
    ):
        self.list_tail = list_tail
        self.message = message

    def validate(self, value: str, field_name: str):
        """
        Validate that the given value does not end with any of the specified suffixes.

        Parameters:
            value (str): The string value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        value = str(value)
        if isinstance(self.list_tail, tuple):
            list_tail = tuple(map(str, self.list_tail))
        else:
            list_tail = str(self.list_tail)

        if value.endswith(list_tail):
            return self.message.format_map(
                defaultdict(
                    str, field_name=field_name, value=value, list_tail=self.list_tail
                )
            )
        return None


class EndWith:
    """
    Validate that a string value ends with one of the specified suffixes.

    Attributes:
        list_tail (list of str): The list of suffixes that the string should end with.
        message (str): The error message template if validation fails.
    """

    def __init__(
        self,
        list_tail: tuple[str],
        message="field {field_name} must be end with {list_tail}",
    ):
        self.list_tail = list_tail
        self.message = message

    def validate(self, value: str, field_name: str):
        """
        Validate that the given value ends with one of the specified suffixes.

        Parameters:
            value (str): The string value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        value = str(value)
        if isinstance(self.list_tail, tuple):
            list_tail = tuple(map(str, self.list_tail))
        else:
            list_tail = str(self.list_tail)

        if not value.endswith(list_tail):
            return self.message.format_map(
                defaultdict(
                    str, field_name=field_name, value=value, list_tail=self.list_tail
                )
            )
        return None


class Equals:
    """
    Validate that a string value is equal to another specified value.

    Attributes:
        another_value (str): The value to compare against.
        message (str): The error message template if validation fails.
    """

    def __init__(
        self,
        another_value: str,
        message="{field_name} must be equal to {another_value}",
    ):
        self.another_value = another_value
        self.message = message

    def validate(self, value: str, field_name: str):
        """
        Validate that the given value is equal to another specified value.

        Parameters:
            value (str): The string value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        if str(value) != str(self.another_value):
            return self.message.format_map(
                defaultdict(
                    str,
                    field_name=field_name,
                    value=value,
                    another_value=self.another_value,
                )
            )
        return None


class NotEquals:
    """
    Validate that a string value is not equal to another specified value.

    Attributes:
        another_value: The value to compare against.
        message (str): The error message template if validation fails.
    """

    def __init__(
        self,
        another_value,
        message="{field_name} must be not same with {another_value}",
    ):
        self.another_value = another_value
        self.message = message

    def validate(self, value: str, field_name: str):
        """
        Validate that the given value is not equal to another specified value.

        Parameters:
            value (str): The string value to validate.
            field_name (str): The name of the field being validated.

        Returns:
            str or None: The error message if validation fails, None otherwise.
        """
        if str(value) == str(self.another_value):
            return self.message.format_map(
                defaultdict(
                    str,
                    field_name=field_name,
                    value=value,
                    another_value=self.another_value,
                )
            )
        return None
