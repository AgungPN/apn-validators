# Customize

## Custom Error Message
We can custom error messages for all validators. Here is an example of how to customize error messages for the `Password` validator.

```python
# common ways custom error messages
Numeric(message="Value should be a number").validate(5.2,'data')
# example Password
Password(messages={"numbers": "one number"})
```

!!! note "Note"
    Only the password rule has different ways to customize error messages.


## Custom Rule
- We can create custom rules by create a class that has a `validate` method.
- in the `validate` method must has two parameters `value` and `field_name`. 
- The `value` is the data that we want to validate and the `field_name` is the name of the field that we want to validate.
- The `validate` method must return `None` if the data is valid, otherwise return the error message (`string`).

```python
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
```

see at [example](/apn-validators/how-to-use) how to use the custom rule.
