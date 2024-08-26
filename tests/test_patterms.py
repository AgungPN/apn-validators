import pytest

from apn_validators.rules.pattern_validators import *


@pytest.mark.parametrize(
    "value,kwargs, expected",
    [
        ("Password123_", {}, None),
        (
            "Password123",
            {},
            "password field must include at least one uppercase letter, one lowercase letter, one digit, one symbol, be at least 8 characters",
        ),
        ("Password123", {"symbols": False}, None),
        (
            "myadmin",
            {
                "symbols": False,
                "messages": {
                    "base_message": "{field_name} harus berisi setidaknya {messages}",
                    "uppercase": "satu huruf besar",
                    "lowercase": "satu huruf kecil",
                    "numbers": "satuan angka",
                    "symbols": "satuan simbol",
                    "length": "minimal {length} karakter",
                },
            },
            "password harus berisi setidaknya satu huruf besar, satu huruf kecil, satuan angka, minimal 8 karakter",
        ),
        (
            "password",
            {"symbols": False, "numbers": False, "uppercase": False, "length": 5},
            None,
        ),
        (
            "",
            {},
            "password field must include at least one uppercase letter, one lowercase letter, one digit, one symbol, be at least 8 characters",
        ),
    ],
)
def test_password(value, kwargs, expected):
    assert Password(**kwargs).validate(value, "password") == expected


@pytest.mark.parametrize(
    "value,kwargs,expected",
    [
        ("test@domain.com", {}, None),
        ("strange.email@sub.domain.com", {}, None),
        ("user@127.loopback.local", {}, None),
        ("sample@domain-with-hyphens.com", {}, None),
        ("user@site-with---hyphens.org", {}, None),
        # ("demo@internationalized-domain.مثال.اختبار", {}, None),
        ("contact@localhost.local", {}, None),
        # ("üser@domain.com", {}, None),
        # ("Łókaść@email.com", {}, None),
        ("email@simpledomain.net", {}, None),
        ('"special\\user"@domain.com', {}, None),
        ('"\\\011"@email.com', {}, None),
    ],
)
def test_email(value, kwargs, expected):
    assert Email(**kwargs).validate(value, "email") == expected


@pytest.mark.parametrize(
    "value,pattern,expected",
    [
        ("2024-08-23", r"^\d{4}-\d{2}-\d{2}$", None),
        (
            "08/23/2024",
            r"^\d{4}-\d{2}-\d{2}$",
            "data field must match with this pattern ^\\d{4}-\\d{2}-\\d{2}$",
        ),
        (
            "Hello123",
            r"^[A-Za-z]+$",
            "data field must match with this pattern ^[A-Za-z]+$",
        ),
        ("HelloWorld", r"^[A-Za-z]+$", None),
    ],
)
def test_match_regex(value, pattern, expected):
    assert MatchRegex(pattern).validate(value, "data") == expected


@pytest.mark.parametrize(
    "value,pattern,expected",
    [
        (
            "2024-08-23",
            r"^\d{4}-\d{2}-\d{2}$",
            "data field must not match with this pattern ^\\d{4}-\\d{2}-\\d{2}$",
        ),
        ("08/23/2024", r"^\d{4}-\d{2}-\d{2}$", None),
        ("Hello123", r"^[A-Za-z]+$", None),
        (
            "HelloWorld",
            r"^[A-Za-z]+$",
            "data field must not match with this pattern ^[A-Za-z]+$",
        ),
    ],
)
def test_not_match_regex(value, pattern, expected):
    assert NotMatchRegex(pattern).validate(value, "data") == expected
