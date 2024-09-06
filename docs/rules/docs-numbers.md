# Number Rules

## Numberic

check if the value is a number or not, it can be integer, float, or string can be convert to integer or float.

##### Parameters:

- message (str, optional): The error message to be used if the validation fails.

??? example Example

    ```python
    # single validate
    Numeric().validate(5,'data')
    # using custom error message
    Numeric(message="Value should be a number").validate(5.2,'data')
    ```

## GreaterThenOrEqual

Validator to check if a value is greater than or equal a specified threshold.

`GreaterThenOrEqual` has an alias `Gte`.

##### Parameters:

- threshold (float): The threshold value that the input value must exceed.
- message (str,optional): The error message to be used if the validation fails.

??? example Example

    ```python
    # single validate
    GreaterThenOrEqual(5).validate(5,'data')
    Gte(5) # alias, same as GreaterThenOrEqual(5)
    # using custom error message
    GreaterThenOrEqual(5, message="Value {field_name} should be greater than or equal to {threshold}")
    ```

## GreaterThen

Validator to check if a value is greater than a specified threshold.
`GreaterThen` has an alias `Gt`.

##### Parameters:

- threshold (float): The threshold value that the input value must exceed.
- message (str,optional): The error message to be used if the validation fails.

??? example Example

    ```python
    # single validate
    GreaterThen(5).validate(6,'data')
    Gt(5) # alias, same as GreaterThen(5)
    # using custom error message
    GreaterThen(5, message="Value {field_name} should be greater than {threshold}")
    ```

## LessThenOrEqual

Validator to check if a value is less than or equal a specified threshold.

`LessThenOrEqual` has an alias `Lte`.

##### Parameters:

- threshold (float): The threshold value that the input value must exceed.
- message (str,optional): The error message to be used if the validation fails.

??? example Example

    ```python
    # single validate
    LessThenOrEqual(5).validate(5,'data')
    Lte(5) # alias, same as LessThenOrEqual(5)
    # using custom error message
    LessThenOrEqual(5, message="Value {field_name} should be less than or equal to {threshold}")
    ```

## LessThen

Validator to check if a value is less than a specified threshold.

`LessThen` has an alias `Lt`.

##### Parameters:

- threshold (float): The threshold value that the input value must exceed.
- message (str, optional): The error message to be used if the validation fails.

??? example Example

    ```python
    # single validate
    LessThen(5).validate(4,'data')
    Lt(5) # alias, same as LessThen(5)
    # using custom error message
    LessThen(5, message="Value {field_name} should be less than {threshold}")
    ```

## NumberRange

Validate to check if a value is has number between min and max

##### Parameters:

- min (int|float): The minimum number allowed.
- max (int|float): The maximum number allowed.
- message (str, optional): The error message to be used if the validation fails.

??? example Example

    ```python
    # single validate
    NumberRange(5, 10).validate(6,'data')
    # using custom error message
    NumberRange(5, 10, message="Value {field_name} should be between {min} and {max}")
    ```

## DecimalRange

Validate to check if a value is has decimal between min and max

##### Parameters:

- min (int): The minimum number of decimal places allowed.
- max (int): The maximum number of decimal places allowed.
- message (str): The error message to be used if the validation fails.

??? example Example

    ```python
    # single validate
    # 5.2 has 1 decimal
    DecimalRange(1, 2).validate(5.2,'data')
    ```

## DigitsBetween

Validator to check if a value has a length between a specified minimum and maximum.

> Check by: if **length < min** or **length > max** will return error

##### Parameters:

- min (int): The minimum length that the value must have.
- max (int): The maximum length that the value must have.
- decimal_include (bool): Include decimal or not when calculate length (default: True).
- dot_include (bool): Include dot or not when calculate length (default: False).
- message (str): The error message to be used if the validation fails.

??? example Example

    ```python
    # single validate
    # 123456.34 has 8 digits, cause dot is not include
    DigitsBetween(5, 10,dot_include=False).validate(123456.34,'data')
    # set min=5, max=10, exclude decimal, include dot to count as length
    DigitsBetween(min=5, max=10, decimal_include=False, dot_include=True)
    ```
