import pytest

from apn_validators import validate
from apn_validators.rules.number_validators import *


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("10", {}, None),
        ("-10", {}, None),
        (10, {}, None),
        (-10, {}, None),
        ("10.5", {}, None),
        ("-10.5", {}, None),
        (10.5, {}, None),
        (-10.5, {}, None),
        (0.0, {}, None),
        ("10a", {}, "data only accept numbers"),
        ("a10", {}, "data only accept numbers"),
        ("1a0", {}, "data only accept numbers"),
    ],
)
def test_numeric(value, kargs, expected):
    # single validation
    assert Numeric(**kargs).validate(value, "data") == expected

    # multi validations
    _, err = validate({"data": [Numeric(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("10", {"threshold": 10}, None),
        ("-10", {"threshold": -20}, None),
        (10, {"threshold": 5}, None),
        (-10, {"threshold": -10}, None),
        ("10.5", {"threshold": 10}, None),
        ("-10.5", {"threshold": -10.5}, None),
        (10.5, {"threshold": 10}, None),
        (-10.5, {"threshold": -11}, None),
        (
            10.5,
            {"threshold": 10.6},
            "field data should be number and greater then or equal to 10.6",
        ),
        (
            "10a",
            {"threshold": 10},
            "field data should be number and greater then or equal to 10",
        ),
        (
            "a10",
            {"threshold": 10},
            "field data should be number and greater then or equal to 10",
        ),
        (
            "1a0",
            {"threshold": 10},
            "field data should be number and greater then or equal to 10",
        ),
    ],
)
def test_greater_then_or_equals(value, kargs, expected):
    # single validate
    assert GreaterThenOrEqual(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [Gte(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("10", {"threshold": 9}, None),
        ("-10", {"threshold": -21}, None),
        (10, {"threshold": 5}, None),
        (-10, {"threshold": -11}, None),
        ("10.5", {"threshold": 10}, None),
        ("10.5", {"threshold": 10.4}, None),
        (10.5, {"threshold": 10}, None),
        (-10.5, {"threshold": -11}, None),
        (
            10.5,
            {"threshold": 10.6},
            "field data should be number and greater then 10.6",
        ),
        (
            "10a",
            {"threshold": 10},
            "field data should be number and greater then 10",
        ),
        (
            "a10",
            {"threshold": 10},
            "field data should be number and greater then 10",
        ),
        (
            "1a0",
            {"threshold": 10},
            "field data should be number and greater then 10",
        ),
    ],
)
def test_greater_than(value, kargs, expected):
    # single validate
    assert GreaterThen(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [Gt(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("10", {"threshold": 10}, None),
        ("-10", {"threshold": -2}, None),
        (10, {"threshold": 15}, None),
        (-10, {"threshold": -10}, None),
        ("10.5", {"threshold": 11}, None),
        ("10.5", {"threshold": 10.6}, None),
        (10.5, {"threshold": 10.5}, None),
        (-10.5, {"threshold": -10}, None),
        (
            10.5,
            {"threshold": 10.4},
            "field data should be number and less then or equal to 10.4",
        ),
        (
            "10a",
            {"threshold": 10},
            "field data should be number and less then or equal to 10",
        ),
        (
            "a10",
            {"threshold": 10},
            "field data should be number and less then or equal to 10",
        ),
        (
            "1a0",
            {"threshold": 10},
            "field data should be number and less then or equal to 10",
        ),
    ],
)
def test_less_than_or_equal(value, kargs, expected):
    # single validate
    assert LessThenOrEqual(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [Lte(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("10", {"threshold": 11}, None),
        ("-10", {"threshold": -2}, None),
        (10, {"threshold": 15}, None),
        (-10, {"threshold": -9}, None),
        ("10.5", {"threshold": 11}, None),
        ("10.5", {"threshold": 10.6}, None),
        (10.5, {"threshold": 11}, None),
        (-10.5, {"threshold": -10}, None),
        (
            10.5,
            {"threshold": 10.4},
            "field data must be number and less then 10.4",
        ),
        (
            "10a",
            {"threshold": 10},
            "field data must be number and less then 10",
        ),
        (
            "a10",
            {"threshold": 10},
            "field data must be number and less then 10",
        ),
        (
            "1a0",
            {"threshold": 10},
            "field data must be number and less then 10",
        ),
    ],
)
def test_less_than(value, kargs, expected):
    # single validate
    assert LessThen(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [Lt(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("10", {"min": 9, "max": 11}, None),
        (10, {"min": 9, "max": 11}, None),
        (3.7, {"min": 3.6, "max": 4}, None),
        (-3.7, {"min": -3.8, "max": 4}, None),
        (3.7, {"min": 3.8, "max": 4}, "field data must be between from 3.8 and 4"),
    ],
)
def test_number_range(value, kargs, expected):
    # single validate
    assert NumberRange(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [NumberRange(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


# @pytest.mark.parametrize(
#     "value,kargs,expected",
#     [
#         ("1.1", {"min": 1, "max": 1}, None),
#         (3.14, {"min": 1, "max": 2}, None),
#         (
#             3,
#             {"min": 2, "max": 2},
#             "error",
#         ),  # TODO: still error, must not let empty decimal when set min > 0
#     ],
# )
# def test_decimal_range(value, kargs, expected):
#     # single validate
#     assert DecimalRange(**kargs).validate(value, "data") == expected
#     # multi validations
#     _, err = validate({"data": [DecimalRange(**kargs)]}, {"data": value}, True)
#     if expected is None:
#         assert err == []
#     else:
#         assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("1.1", {"min": 1, "max": 2}, None),
        ("1", {"min": 1, "max": 1}, None),
        (1.1, {"min": 1, "max": 2}, None),
        (1, {"min": 1, "max": 1}, None),
        (3.14, {"min": 1, "max": 3}, None),
        (
            3.14,
            {"min": 4, "max": 4, "digit_include": True, "dot_include": True},
            None,
        ),
        (
            3.14,
            {"min": 1, "max": 2, "digit_include": True},
            "field data must have a length between 1 and 2",
        ),
    ],
)
def test_digits_between(value, kargs, expected):
    # single validate
    assert DigitsBetween(**kargs).validate(value, "data") == expected
    # multi validations
    _, err = validate({"data": [DigitsBetween(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err
