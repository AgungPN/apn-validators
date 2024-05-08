class Validator:
    _field_name = "field"
    _value = None
    _instance = None
    _errors = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def set_field(cls, field_name):
        """
        Set the field name.

        Parameters:
            field_name (str): The name of the field.

        Returns:
            None
        """
        cls._instance._field_name = field_name

    @classmethod
    def set_value(cls, value):
        """
        Set the value.

        Parameters:
            value: The value to set.

        Returns:
            None
        """
        cls._instance._value = value

    @classmethod
    def set_field_and_value(cls, field_name, value):
        """
        Set both the field name and value.

        Parameters:
            field_name (str): The name of the field.
            value: The value to set.

        Returns:
            None
        """
        cls._instance._field_name = field_name
        cls._instance._value = value

    @classmethod
    def _get_field(cls, field_name):
        """
        Get the field name.

        Parameters:
            field_name (str): The name of the field.

        Returns:
            str: The name of the field.
        """
        return cls._instance._field_name if field_name is None else field_name

    @classmethod
    def _get_field_and_value(cls, field_name, value):
        """
        Get the field name and value.

        Parameters:
            field_name (str): The name of the field.
            value: The value.

        Returns:
            tuple: A tuple containing the field name and value.
        """
        field_name = field_name if field_name is not None else cls._instance._field_name
        value = value if value is not None else cls._instance._value
        return field_name, value

    @classmethod
    def reset_field_and_value(cls):
        """
        Reset the field name and value.

        Returns:
            None
        """
        cls._instance._field_name = []
        cls._instance._value = None

    @classmethod
    def add_error(cls, field_name: str, error: str):
        """
        Add an error message.

        Parameters:
            field_name (str): The name of the field.
            error (str): The error message.

        Returns:
            None
        """
        cls._instance._errors.append((field_name, error))

    @classmethod
    def get_errors(cls, is_group_by_field: bool = False):
        """
        Retrieve the list of error messages.

        Parameters:
            is_group_by_field (bool, optional): If True, group error messages by field name. If False, return a list of error messages (default: False).

        Returns:
            list or dict: If is_group_by_field is False, returns a list of error messages. If is_group_by_field is True, returns a dictionary where keys are field names and values are lists of error messages.
        """
        response = None
        if is_group_by_field:
            group_by_field = {}
            for field, message in cls._instance._errors:
                if field in group_by_field:
                    group_by_field[field].append(message)
                else:
                    group_by_field[field] = [message]
            response = group_by_field
        else:
            response = [message for _, message in cls._instance._errors]

        # Reset errors
        cls._instance._errors = []

        return response


_instance_validator = Validator()


def start_validator():
    """starting the validator"""
    global _instance_validator
    _instance_validator = Validator()
    return _instance_validator


if __name__ == "__main__":
    # Test the singleton pattern
    validator1 = Validator()
    validator2 = Validator()
    validator3 = Validator()

    validator1.add_error("email", "Invalid email format")

    print(id(validator1) == id(validator2) == id(validator3))
