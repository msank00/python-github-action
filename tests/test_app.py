from app import welcome


def test_welcome():
    assert welcome() == "Hello, world!"