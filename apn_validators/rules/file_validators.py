from collections import defaultdict


class AllowedFile:
    """
    Validate that a file has a valid extension.

    Parameters:
        allowed_extensions (set, optional): A set of allowed file extensions in lowercase (default: {"png", "jpg", "jpeg"}).
    """

    def __init__(
        self,
        allowed_extensions=None,
        message="{field_name} only accepts {allowed_extensions}",
    ):
        self.allowed_extensions = allowed_extensions or {"png", "jpg", "jpeg"}
        self.message = message

    def validate(self, file_name, field_name):
        """
        Validate the file name.

        Parameters:
            file_name (str): The name of the file.
            field_name (str): The name of the field being validated .

        Returns:
            str: Error message if validation fails, None otherwise.
        """

        # if not set file then return none. If want to be required, then add rules NotBlank()
        if file_name is None:
            return None
        if file_name.strip() == "":
            return None

        if (
            "." in file_name
            and file_name.rsplit(".", 1)[1].lower() in self.allowed_extensions
        ):
            return None

        return self.message.format_map(
            defaultdict(
                str, field_name=field_name, allowed_extensions=self.allowed_extensions
            )
        )


if __name__ == "__main__":
    print(AllowedFile().validate("1.png", "file"))
    print(AllowedFile().validate("1.docs", "file"))
    print(AllowedFile().validate("1docs", "file"))
    print(AllowedFile().validate("", "file"))
