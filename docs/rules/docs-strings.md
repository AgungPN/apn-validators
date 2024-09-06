# String Rules

## Length

Validator to check if the length of a string value falls within a specified range.

##### Parameters:

- min_length (int): The minimum allowed length of the string.
- max_length (int): The maximum allowed length of the string.
- message (str): The error message to be used if the validation fails.

??? example Example

    ```python
    Length(5, 10) # Length(min_length=5, max_length=10)
    ```

## MinLength

Validator to check if a value has a minimum length.

##### Parameters:

- min (int): The minimum length that the value must have.
- message (str): The error message to be used if the validation fails.

??? example Example

    ```python
    MinLength(5) # MinLength(min=5)
    ```

## MaxLength

Validator to check if a value has a maximum length.

##### Parameters:

- max (int): The maximum length that the value must have.
- message (str): The error message to be used if the validation fails.

??? example Example

    ```python
    MaxLength(10) # MaxLength(max=10)
    ```

## NotBlank

Validator to check if a string value is not blank (empty or contains only whitespace).

##### Parameters:

- message (str): The error message to be used if the validation fails.

??? example Example

    ```python
    NotBlank()
    # custom error message
    NotBlank(message="Value should not be blank")
    ```

## InList

Validator to check if a string value is present in a specified list.

##### Parameters:

- valid_values (list): The list of valid values.
- message (str): The error message to be used if the validation fails.

??? example Example

    ```python
    InList(["apple", "banana", "cherry"])
    # custom error message
    InList(["apple", "banana", "cherry"], "Value {field_name} should be one of: {valid_values}")
    ```

## NotInList

Validator to check if a string value is not present in a specified list.

##### Parameters:

- invalid_values (list): The list of invalid values.
- message (str): The error message to be used if the validation fails.

??? example Example

    ```python
    NotInList(["apple", "banana", "cherry"])
    # custom error message
    NotInList(["apple", "banana", "cherry"], "Value {field_name} should not be one of: {valid_values}")
    ```

## DoesntStartsWith

Validate that a string value does not start with any of the specified prefixes.

##### Parameters:

- list_prefix (list of str): The list of prefixes that the string should not start with.
- message (str): The error message template if validation fails.

??? example Example

    ```python
    DoesntStartsWith(["apple", "banana", "cherry"])
    # custom error message
    DoesntStartsWith(["apple", "banana", "cherry"], "Value {field_name} should not start with any of: {list_prefix}")
    ```

## StartsWith

Validate that a string value does not start with any of the specified prefixes.

##### Parameters:

- list_prefix (list of str): The list of prefixes that the string should not start with.
- message (str): The error message template if validation fails.

??? example Example

    ```python
    StartsWith(["apple", "banana", "cherry"])
    # custom error message
    StartsWith(["apple", "banana", "cherry"], "Value {field_name} should start with any of: {list_prefix}")
    ```

## DoesntEndsWith
Validate that a string value does not start with any of the specified prefixes.

##### Parameters:
- list_prefix (list of str): The list of prefixes that the string should not start with.
- message (str): The error message template if validation fails.

??? example Example

    ```python
    DoesntEndsWith(["apple", "banana", "cherry"])
    # custom error message
    DoesntEndsWith(["apple", "banana", "cherry"], "Value {field_name} should not end with any of: {list_prefix}")
    ```

## EndsWith
Validate that a string value ends with one of the specified suffixes.

##### Parameters:
- list_tail (list of str): The list of suffixes that the string should end with.
- message (str): The error message template if validation fails.

??? example Example
    ```python
    EndsWith(["apple", "banana", "cherry"])
    # custom error message
    EndsWith(["apple", "banana", "cherry"], "Value {field_name} should end with any of: {list_tail}")
    ```

## Equals
Validate that a string value is equal to another specified value.

##### Parameters:
- another_value (str): The value to compare against.
- message (str): The error message template if validation fails.

??? example Example
    ```python
    Equals("apple")
    # custom error message
    Equals("apple", "Value {field_name} should be equal to {another_value}")
    ```

## NotEquals
Validate that a string value is not equal to another specified value.

##### Parameters:
- another_value: The value to compare against.
- message (str): The error message template if validation fails.

??? example Example
    ```python
    NotEquals("apple")
    # custom error message
    NotEquals("apple", "Value {field_name} should not be equal to {another_value}")
    ```
