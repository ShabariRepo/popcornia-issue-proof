from slug import slugify


def test_simple():
    assert slugify("Hello World") == "hello-world"


def test_punctuation_and_repeated_spaces():
    assert slugify("Hello,  World!") == "hello-world"


def test_tab():
    assert slugify("a\tb") == "a-b"


def test_no_dashes_at_ends():
    assert slugify("  --Hello--  ") == "hello"
