import pytest

from apn_validators import validate
from apn_validators.rules.file_validators import *


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("1.png", {}, None),
        ("1.e.g.png", {}, None),
        ("1.e.g.txt", {"allowed_extensions": ("png", "txt")}, None),
        ("1.docs", {}, "file only accepts ('png', 'jpg', 'jpeg')"),
        ("1docs", {}, "file only accepts ('png', 'jpg', 'jpeg')"),
        ("", {}, None),
    ],
)
def test_allowed_file(value, kargs, expected):
    assert AllowedFile(**kargs).validate(value, "file") == expected
    _, err = validate({"file": [AllowedFile(**kargs)]}, {"file": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err
