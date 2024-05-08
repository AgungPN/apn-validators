import validators

check_validation = validators.start_validator()
validators.password(value="apn124")

print(check_validation.get_errors())
