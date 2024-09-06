# Date Rules

## IsDate

must be a valid date

##### Parameters:

- date_format (str, optional): The date format to be used for validation. If not provided, the default format is `%Y-%m-%d`.
- **message** (str, optional): The error message to be used if the validation fails.

??? example Example

    ```python
    # single validate, using default date format
    IsDate().validate("2020-01-01", "data")
    IsDate(date_format="%Y-%m-%d")
    ```

## DateEquals

Validate that the provided date value is equal to the target date.

###### Parameters:

- target_date: (datetime.date) the date to compare against
- date_format: (str,optional) the date format to validate the date against (default: %Y-%m-%d)
- message: (str,optional) the error message to return if the validation fails

??? example Example

    ```python
    # single validate, using default date format
    DateEquals(datetime.datetime.strptime("2024-12-24", "%Y-%m-%d")).validate("2024-12-24", "data")
    ```

## DateAfter

Validate that the provided date value is after the target date.

##### Parameters:

- target_date: (datetime.date) the date to compare against
- date_format: (str,optional) the date format to validate the date against (default: %Y-%m-%d)
- message: (str,optional) the error message to return if the validation

??? example Example

    ```python
    DateAfter(datetime.datetime.strptime("2024-12-24", "%Y-%m-%d")).validate("2024-12-25", "data")
    ```

## DateBefore

Validate that the provided date value is before the target date.

##### Parameters:

- target_date: (datetime.date) the date to compare against
- date_format: (str,optional) the date format to validate the date against (default: %Y-%m-%d)
- message: (str,optional) the error message to return if the validation

??? example Example

    ```python
    DateBefore(datetime.datetime.strptime("2024-12-24", "%Y-%m-%d")).validate("2024-12-22", "data")
    ```
