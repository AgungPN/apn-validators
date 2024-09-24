from datetime import datetime

import pytest

from apn_validators import validate
from apn_validators.rules.date_validators import *

todayDate = datetime.date.today()
tomorrowDate = todayDate + datetime.timedelta(days=1)
yesterdayDate = todayDate - datetime.timedelta(days=1)


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        ("2024-12-24", {}, None),
        ("2024/12/24", {"date_format": "%Y/%m/%d"}, None),
        ("2024/12/24", {}, "field data is not a valid date"),
        ("2024-22-24", {}, "field data is not a valid date"),
    ],
)
def test_is_date(value, kargs, expected):
    assert IsDate(**kargs).validate(value, "data") == expected
    _, err = validate({"data": [IsDate(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        (
            "2024-12-24",
            {"target_date": datetime.datetime.strptime("2024-12-24", "%Y-%m-%d")},
            None,
        ),
        (
            "2024/12/24",
            {
                "target_date": datetime.datetime.strptime("2024/12/24", "%Y/%m/%d"),
                "date_format": "%Y/%m/%d",
            },
            None,
        ),
        (
            "2024-02-24",
            {"target_date": datetime.datetime.strptime("2024-12-12", "%Y-%m-%d")},
            "field data must be equal to 2024-12-12",
        ),
        (
            todayDate.strftime("%Y-%m-%d"),
            {"target_date": "today"},
            None,
        ),
        (
            "2024/12/24",
            {
                "target_date": "2024/12/24",
                "date_format": "%Y/%m/%d",
            },
            None,
        ),
    ],
)
def test_date_equals(value, kargs, expected):
    assert DateEquals(**kargs).validate(value, "data") == expected
    _, err = validate({"data": [DateEquals(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        (
            "2024-12-25",
            {"target_date": datetime.datetime.strptime("2024-12-24", "%Y-%m-%d")},
            None,
        ),
        (
            "2024/12/25",
            {
                "target_date": datetime.datetime.strptime("2024/12/24", "%Y/%m/%d"),
                "date_format": "%Y/%m/%d",
            },
            None,
        ),
        (
            "2024-02-24",
            {"target_date": datetime.datetime.strptime("2024-12-12", "%Y-%m-%d")},
            "field data must be after 2024-12-12",
        ),
        (
            tomorrowDate.strftime("%Y-%m-%d"),
            {"target_date": "yesterday"},
            None,
        ),
        (
            "2024/12/25",
            {
                "target_date": "2024/12/24",
                "date_format": "%Y/%m/%d",
            },
            None,
        ),
    ],
)
def test_date_after(value, kargs, expected):
    assert DateAfter(**kargs).validate(value, "data") == expected
    _, err = validate({"data": [DateAfter(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err


@pytest.mark.parametrize(
    "value,kargs,expected",
    [
        (
            "2024-12-23",
            {"target_date": datetime.datetime.strptime("2024-12-24", "%Y-%m-%d")},
            None,
        ),
        (
            "2024/12/23",
            {
                "target_date": datetime.datetime.strptime("2024/12/24", "%Y/%m/%d"),
                "date_format": "%Y/%m/%d",
            },
            None,
        ),
        (
            "2024-12-24",
            {"target_date": datetime.datetime.strptime("2024-12-12", "%Y-%m-%d")},
            "field data must be before 2024-12-12",
        ),
        (
            yesterdayDate.strftime("%Y-%m-%d"),
            {"target_date": "tomorrow"},
            None,
        ),
        (
            "2024/12/23",
            {
                "target_date": "2024/12/24",
                "date_format": "%Y/%m/%d",
            },
            None,
        ),
    ],
)
def test_date_before(value, kargs, expected):
    assert DateBefore(**kargs).validate(value, "data") == expected
    _, err = validate({"data": [DateBefore(**kargs)]}, {"data": value}, True)
    if expected is None:
        assert err == []
    else:
        assert expected in err
