# Getting Started

The Validation Package provides a robust and extensible framework for validating data in Python applications. *Designed with flexibility and scalability in mind*, it offers a suite of pre-built validators and supports custom validation logic. This package ensures data integrity and simplifies the process of enforcing business rules across various domains.


## Key Features

- **Modular Design**: Each validator is encapsulated in its own class, making it easy to manage and extend the validation logic.
- **Customizable Error Messages**: Validators support customizable error messages, allowing for clear and context-specific feedback.
- **Customizable Schema**: Users can create their own validation schemas according to their specific needs, providing flexibility to handle unique validation scenarios.
- **Comprehensive Validation Suite**: Includes a wide range of validators for common data validation tasks such as length checks, format verification, numerical comparisons, list inclusion, regular expression matching, etc.


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

