import pytest

from apn_validators import validate
from apn_validators.rules.string_validators import *


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("hello world", {"min": 5, "max": 20}, None),
        ("hello-world", {"min": 11, "max": 11}, None),
        ("hello world", {"min": 11, "max": 11}, None),
        ("", {"min": 0, "max": 10}, None),
        (1111, {"min": 0, "max": 4}, None),
        ("hello", {"min": 0, "max": 4}, "field data length must be between 0 and 4"),
    ],
)
def test_length(value, kargs, expected):
    # single validation
    assert Length(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [Length(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("hello world", {"min": 5}, None),
        ("hello-world", {"min": 11}, None),
        ("hello world", {"min": 11}, None),
        ("", {"min": 0}, None),
        (1111, {"min": 4}, None),
        ("hello", {"min": 10}, "field data must have a minimum length of 10"),
    ],
)
def test_min_length(value, kargs, expected):
    # single validation
    assert MinLength(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [MinLength(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("hello world", {"max": 20}, None),
        ("hello-world", {"max": 11}, None),
        ("hello world", {"max": 11}, None),
        ("", {"max": 10}, None),
        (1111, {"max": 4}, None),
        ("hello", {"max": 4}, "field data must have a maximum length of 4"),
    ],
)
def test_max_length(value, kargs, expected):
    # single validation
    assert MaxLength(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [MaxLength(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("hello world", {}, None),
        (1, {}, None),
        (0, {}, None),
        (0.0, {}, None),
        (False, {}, None),
        ("", {}, "field data must not be blank"),
        ("    ", {}, "field data must not be blank"),
        (None, {}, "field data must not be blank"),
    ],
)
def test_not_blank(value, kargs, expected):
    # single validation
    assert NotBlank(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [NotBlank(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("hello", {"valid_values": ["hello", "world"]}, None),
        ("world", {"valid_values": ["hello", "world"]}, None),
        (1, {"valid_values": [1, 2, 3]}, None),
        (1, {"valid_values": [1]}, None),
        (1, {"valid_values": ["1"]}, None),
        ("1", {"valid_values": [1]}, None),
        (
            "",
            {"valid_values": ["hello", "world"]},
            "field data must be in ['hello', 'world']",
        ),
    ],
)
def test_in_list(value, kargs, expected):
    # single validation
    assert InList(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [InList(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("hey", {"invalid_values": ["hello", "world"]}, None),
        (
            "WORLD",
            {"invalid_values": ["hello", "world"]},
            None,
        ),  # TODO: add new options to make case insensitive
        (4, {"invalid_values": [1, 2, 3]}, None),
        (4, {"invalid_values": [1]}, None),
        (4, {"invalid_values": ["44"]}, None),
        ("1", {"invalid_values": [44]}, None),
        ("", {"invalid_values": ["hello", "world"]}, None),
        (
            "hello",
            {"invalid_values": ["hello", "world"]},
            "field data must not be in ['hello', 'world']",
        ),
    ],
)
def test_not_in_list(value, kargs, expected):
    # single validation
    assert NotInList(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [NotInList(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("hello world", {"list_prefix": ("hey")}, None),
        # (
        #     "HELLO world",
        #     {"list_prefix": ("hello")},
        #     None,
        # ),  # TODO: make option to make case insensitive
        ("hello-world", {"list_prefix": ("hey")}, None),
        (
            "hello world",
            {"list_prefix": ("hello", "test")},
            "field data must not be start with ('hello', 'test')",
        ),
        ("", {"list_prefix": ("a", "b")}, None),
        (10, {"list_prefix": (11)}, None),
        (
            0,
            {"list_prefix": (0, 2, "a")},
            "field data must not be start with (0, 2, 'a')",
        ),
    ],
)
def test_doesnt_start_with(value, kargs, expected):
    # single validation
    assert DoesntStartsWith(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [DoesntStartsWith(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("hello world", {"list_prefix": ("hello")}, None),
        # (
        #     "HELLO world",
        #     {"list_prefix": ("hello")},
        #     None,
        # ),  # TODO: make option to make case insensitive
        ("hello-world", {"list_prefix": ("hello")}, None),
        (
            "hello world",
            {"list_prefix": ("world")},
            "field data must be start with world",
        ),
        (
            "hello world",
            {"list_prefix": ("world", "test")},
            "field data must be start with ('world', 'test')",
        ),
        ("", {"list_prefix": ("")}, None),
        (10, {"list_prefix": (1)}, None),
        (
            0,
            {"list_prefix": (1, 2, "a")},
            "field data must be start with (1, 2, 'a')",
        ),
    ],
)
def test_start_with(value, kargs, expected):
    # single validation
    assert StartsWith(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [StartsWith(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("hello world", {"list_tail": ("hey")}, None),
        # (
        #     "HELLO world",
        #     {"list_tail": ("hello")},
        #     None,
        # ),  # TODO: make option to make case insensitive
        ("hello-world", {"list_tail": ("hey")}, None),
        (
            "hello world",
            {"list_tail": ("world", "test")},
            "field data must not be end with ('world', 'test')",
        ),
        ("", {"list_tail": ("a", "b")}, None),
        (21, {"list_tail": (2)}, None),
        (
            0,
            {"list_tail": (0, 2, "a")},
            "field data must not be end with (0, 2, 'a')",
        ),
    ],
)
def test_doesnt_ends_with(value, kargs, expected):
    # single validation
    assert DoesntEndsWith(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [DoesntEndsWith(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("hello world", {"list_tail": ("world")}, None),
        # (
        #     "HELLO world",
        #     {"list_tail": ("hello")},
        #     None,
        # ),  # TODO: make option to make case insensitive
        ("hello-world", {"list_tail": ("-world")}, None),
        (
            "hello world",
            {"list_tail": ("hello")},
            "field data must be end with hello",
        ),
        (
            "hello world",
            {"list_tail": ("worl", "test")},
            "field data must be end with ('worl', 'test')",
        ),
        ("", {"list_tail": ("")}, None),
        (10, {"list_tail": (0)}, None),
        (
            0,
            {"list_tail": (1, 2, "a")},
            "field data must be end with (1, 2, 'a')",
        ),
    ],
)
def test_ends_with(value, kargs, expected):
    # single validation
    assert EndsWith(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [EndsWith(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


# TODO: equals and not equals
