# File Rules

## AllowedExtensions
Validate that a file has a valid extension.

##### Parameters:
- **allowed_extensions **(list, optional): A set of allowed file extensions in lowercase (*default: {"png", "jpg", "jpeg"}*).
- **message** (str, optional): The error message to be used if the validation fails.

??? example Example
    ```python
    # single validate
    AllowedExtensions().validate("file.png", "data")
    # using custom allowed extensions
    AllowedExtensions(allowed_extensions=["pdf", "doc"]).validate("file.pdf", "data")
    ```
