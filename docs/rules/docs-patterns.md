# Pattern Rules

## Password

Validate that a string is a valid password based on various criteria.

##### Parameters:

- **uppercase** (_bool, optional_): Whether the password must contain uppercase letters (default: True).
- **lowercase** (_bool, optional_): Whether the password must contain lowercase letters (default: True).
- **numbers** (_bool, optional_): Whether the password must contain numeric digits (default: True).
- **symbols** (_bool, optional_): Whether the password must contain symbols (default: True).
- **length** (_int, optional_): The minimum length of the password (default: 8).
- **messages** (_dict[str,str],optional_): custom error message

> message has this default value

```python
{
    "base_message": "{field_name} field must include at least {messages}",
    "uppercase": "one uppercase letter",
    "lowercase": "one lowercase letter",
    "numbers": "one digit",
    "symbols": "one symbol",
    "length": "be at least {length} characters",
}
```

??? example Example

    this is simple example of how to use Password validator

    ```python
    # using default config
    Password()
    # using default but make it 10 characters long and require symbols
    Password(symbols=False, length=10)
    # using custom error messages
    # only chstomize numbers error message. But we can customize all messages
    Password(messages={"numbers": "one number"})
    ```

## Email

Validate that a string value is a valid email address.

##### Parameters:

- **message** (_str,optional_): The error message to be used if the validation fails.

??? example Example

    ```python
    Email()
    ```

## MatchRegex

Validator to check if a value matches a specified regular expression pattern.

##### Parameters:

- **pattern** (_str_): The regular expression pattern to check against. (_required_)
- **message** (_str,optional_): The error message to be used if the validation fails.

??? example Example
    ```python
    # using default config
    MatchRegex(pattern=r"\d+")
    # using custom error message
    MatchRegex(pattern=r"\d+", message="Value should contain digits")
    ```

## NotMatchRegex

Validator to check if a value does not match a specified regular expression pattern.

##### Parameters:

- **pattern** (_str_): The regular expression pattern to check against. (_required_)
- **message** (_str,optional_): The error message to be used if the validation fails.

??? example Example

    ```python
    # using default config
    NotMatchRegex(pattern=r"\d+")
    # using custom error message
    NotMatchRegex(pattern=r"\d+", message="Value should not contain digits")
    ```
