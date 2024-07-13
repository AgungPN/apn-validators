def err_to_list(errors: dict) -> list:
    """
    Convert a dictionary of error messages to a single list of error messages.

    Parameters:
        errors (dict[list]): A dictionary where keys are field names and values are lists of error messages.

    Returns:
        list: A list of all error messages. If the input is None, returns None. If the input is a string, returns a list containing the string.

    Example:
        errors = {
            'username': ['Username is required', 'Username must be at least 3 characters'],
            'email': ['Email is invalid'],
        }
        error_list = err_to_list(errors)
        # error_list will be ['Username is required', 'Username must be at least 3 characters', 'Email is invalid']
    """
    if errors is None:
        return []

    if isinstance(errors, str):
        return [errors]

    error_messages = []
    for messages in errors.values():
        error_messages.extend(messages)
    return error_messages


def validate(schema: dict, values: dict, is_err_to_list=False):
    """
    Validate the provided values against the specified validation schema.

    Parameters:
        schema (dict): A dictionary where keys are field names and values are lists of validation rule objects.
        values (dict): A dictionary where keys are field names and values are the values to be validated.

    Returns:
        tuple: A tuple containing two dictionaries:
            - validated (dict): A dictionary of the validated field names and their corresponding values.
            - errors (dict): A dictionary where keys are field names and values are lists of error messages for each field.

    Example:
        schema = {
            'username': [NotBlank(), Length(min=3, max=20)],
            'password': [NotBlank(), Password()],
            'email': [Email()],
        }
        values = {
            'username': 'agung_user',
            'password': 's3cr3t!',
            'email': 'agung@example.com',
        }
        validated, err = validate(schema, values)

        if err:
            print("Validation errors:", err)
        else:
            print("All values are valid:", validated)
    """
    errors = {}
    validated = {}

    for field_name, rules in schema.items():
        value = values.get(field_name)
        validated[field_name] = value

        for rule in rules:
            error_message = rule.validate(value, field_name)
            if error_message is not None:
                if errors.get(field_name) is None:
                    errors[field_name] = [error_message]
                else:
                    errors[field_name].append(error_message)

    if is_err_to_list:
        errors = err_to_list(errors)
    return validated, errors
