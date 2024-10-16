"""This module contains the Person Abstract Datatype (ADT).

This class wraps typical spreadsheet information
associated with a person for the ranked-choice matching
task.

Typical usage example:

person = Person(
    name="John Doe",
    email="jd0000@123mail.com",
    choices=["choice_1", "choice_2", "choice_3"],
    top_choice="choice_1",
)
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Person:
    """Wraps the information associated with a person."""

    name: str
    email: str
    choices: list[str]
    top_choice: str
    placement: str = ""


if __name__ == "__main__":
    pass
