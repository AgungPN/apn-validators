# How To Use

## Install

```bash
pip install apn-validators
```

## Using multiple validators

you can use multiple validators to validate multiple fields

`validate` function return tuple of _values and error_

##### Parameters

- `rules` : `dict` - dictionary of fields and list of validators
- `data` : `dict` - dictionary of fields and values
- `is_err_to_list`: `bool`, default `False` - if `True` the error will be a list of string, otherwise the error will be a dictionary

```python
from apn_validators.rules import Password, Email, NotBlank

validated, err =  validate(
    {
        "email": [NotBlank(), Email()],
        "password": [NotBlank(), Password()],
    },
    {"email": "example@example.com", "password": "123456"},
)
```

## Using single validator

you can use a single validator to validate a single field

```python
from apn_validators.rules import Email

err = Email().validate("example@example.com", "email")
if err:
    print(err)

```

## Example

```python
# only import what you need
from apn_validators.rules import Password, Email, Length, NotBlank
from apn_validators import validate

# create a custom rules
class UniqueRule:
    def __init__(self, table, field):
        self.table = table
        self.field = field

    def validate(self, value, field_name):
        # validate data is unique or not
        if not unique:
            return f"{field_name} is not unique"
        return None


# optional to create a function to validate data
def sign_up_request(data):
    # example of how to validate data (multiple fields)
    return validate(
        {
            "email": [NotBlank(), Email()],
            "password": [NotBlank(), Password()],
            "username": [NotBlank(), Length(min=5, max=20), UniqueRule('users','id')],
        },
        data,
    )

# get the values and error (return tuple)
validated, err = sign_up_request(
    {"email": "example@gmail.com", "password": "123456", "username": "example"}
)

# err is trusty if there is an error
if err:
    print(err)

```
