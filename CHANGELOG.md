# Changelog

## Version 0.5

### Other

- Docs: add documentation.
- Test: improve test.
- Feat(file)!: change name rule AllowedFile to AllowedExtensions.
- Feat(date)!: delete DateFormat rule.

### Updates

- Refactor(string)!: change StartWith and EndWith to be plural StarsWith and EndsWith.
- Refactor(number): change digit_include attribute become proper naming to decimal_include in BetweenRule.
- Refactor(Deleted): remove file base_validate.

## Version 0.4

### Fixes

- Fix(Fixed): fixing and improve string validators.
- Fix(Fixed): fixing and improve pattern validators.
- Fix(Fixed): fixing and improve number validators.
- Fix(Fixed): fixing and improve file validators.
- Fix(Fixed): fixing and improve date validators.
- Fix(Added): fix number validation and add NumberRange validator.

### Other

- Build: add pyproject.toml.
- Test(Tested): add feature test".
- Feat(Changed): add feature to custom password message".
- Build: Create python-publish.yml.
- Build: run test app and lint.
- Create LICENSE MIT.
- Feat!: refactor and restructure all rules.
  BREAKING CHANGES: all previous validate structure not longger exists
- Feat: first build.
- Feat: first commit.

### Updates

- Refactor(Deleted): remove file base_validate.
- Refactor!: rename arguments in Length to be more concise.
  Renamed `min_length` and `max_length` parameters to `min` and `max` in `Length` class constructor for better readability and consistency.
