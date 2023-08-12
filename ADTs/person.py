"""This module contains the Person Abstract Datatype (ADT).

Provided a Person's information from a spreadsheet, this class
functions primarily as a wrapper of one's information, their
ranked choices and supports operations.

Typical usage example:

person = Person(name="John Doe",
                id="jd0000",
                choices=["choice1", "choice2", "choice3"])
"""


class Person:
    """A simple class that wraps a person's information."""

    def __init__(self, name: str, id: str, choices: list[str], top_choice: str) -> None:
        self.name = name
        "The person's name."
        self.id = id
        "The person's unique identifier."
        self.choices = choices
        "The person's event choices' names."
        self.top_choice = top_choice
        "The person's top_choice event name."
        return

    def __str__(self) -> str:
        return f"Name: {self.name}; ID: {self.id}"


def main() -> None:
    """Unit Testing"""
    return


if __name__ == "__main__":
    main()
