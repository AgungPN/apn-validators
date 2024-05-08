from .base_validator import _instance_validator


def allowed_file(file_name: str, allowed_extensions=None, field_name=None):
    """
    Validate that a file has a valid extension.

    Parameters:
        file_name (str): The name of the file.
        allowed_extensions (set, optional): A set of allowed file extensions in lowercase (default: {"png", "jpg", "jpeg"}).
        field_name (str, optional): The name of the field being validated (default: None).

    Returns:
        None or String of error
    """
    field_name = _instance_validator._get_field(field_name)
    if allowed_extensions is None:
        allowed_extensions = {"png", "jpg", "jpeg"}

    if file_name.strip() == "":
        _instance_validator.add_error(field_name, f"{file_name} not selected file")
        return

    if "." in file_name and file_name.rsplit(".", 1)[1].lower() in allowed_extensions:
        return

    error_message = f"{field_name} only accepts {allowed_extensions}"
    _instance_validator.add_error(field_name, error_message)
    return error_message
