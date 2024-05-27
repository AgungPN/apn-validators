# APN Validators

The Validation Package provides a robust and extensible framework for validating data in Python applications. Designed with flexibility and scalability in mind, it offers a suite of pre-built validators and supports custom validation logic. This package ensures data integrity and simplifies the process of enforcing business rules across various domains.


## Key Features

- **Modular Design**: Each validator is encapsulated in its own class, making it easy to manage and extend the validation logic.
- **Customizable Error Messages**: Validators support customizable error messages, allowing for clear and context-specific feedback.
- **Customizable Schema**: Users can create their own validation schemas according to their specific needs, providing flexibility to handle unique validation scenarios.
- **Comprehensive Validation Suite**: Includes a wide range of validators for common data validation tasks such as length checks, format verification, numerical comparisons, list inclusion, and regular expression matching.


---

## Requirements

This validation package requires the following dependencies:

- **Python**: Version 3.5 or later is required to use this package.
- **Additional Libraries**:
  - `datetime`: Standard Python library for handling date and time operations.
  - `re`: Standard Python library for handling regular expressions.
  - `collections`: Standard Python library, specifically `defaultdict` from the `collections` module.

Ensure you have Python 3.5 or higher installed on your system. You can check your Python version by running:

```bash
python --version
```
    

## Installation

Install package with [pip](https://pip.pypa.io/en/stable/getting-started/)

```bash
  pip install apn-validators
```


---
### Available Validators

- **Date Validators**:
  - `IsDate` : Ensure value is date
  - `DateAfter`: Ensures a date is after a specified target date.
  ```python

  ```
  - `DateBefore`: Ensures a date is before a specified target date.
  - `DateFormat`: Validates that a date string matches a specified format.

- **String Validators**:
  - `Length`: Checks if the length of a string falls within a specified range.
  - `NotBlank`: Ensures a string is not blank or only contains whitespace.
  - `MatchRegex`: Validates that a string matches a specified regular expression.
  - `NotMatchRegex`: Ensures a string does not match a specified regular expression.
  - `StartWith`: Validates that a string starts with one of the specified prefixes.
  - `DoesntStartWith`: Ensures a string does not start with one of the specified prefixes.
  - `EndWith`: Validates that a string ends with one of the specified suffixes.
  - `DoesntEndWith`: Ensures a string does not end with one of the specified suffixes.
  - `InList`: Checks if a string is present in a specified list.
  - `NotInList`: Ensures a string is not present in a specified list.

- **Numeric Validators**:
  - `Numeric`: Validates that a value is numeric.
  - `GreaterThenOrEqual`: Ensures a value is greater than or equal to a specified threshold.
  - `Decimal`: Validates that a value is numeric and contains the specified number of decimal places.
  - `Digits`: Ensures a value has an exact length.
  - `DigitsBetween`: Validates that the length of a value is within a specified range.
  - `MinDigits`: Ensures a value has a minimum length.
  - `MaxDigits`: Ensures a value has a maximum length.

- **File Validators**:
  - `AllowedFile`: Validates that a file has an allowed extension.

- **Equality Validators**:
  - `Equals`: Validates that a value is equal to another specified value.
