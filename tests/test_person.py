"""This module is responsible for testing the person abstract datatype."""

from ranked_choice_matcher import Person


def test_equality() -> None:
    """Tests person equality."""
    u = Person(
        name="John Doe",
        email="jd0000@123mail.com",
        choices=["choice_1", "choice_2", "choice_3"],
        top_choice="choice_1",
    )
    v = Person(
        name="John Doe",
        email="jd0000@123mail.com",
        choices=["choice_1", "choice_2", "choice_3"],
        top_choice="choice_1",
    )
    assert u == v
    v.placement = "choice_1"
    assert u != v
