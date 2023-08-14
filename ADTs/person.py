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
    """A class wrapping a person's information."""

    def __init__(self, name: str, id: str, choices: list[str], top_choice: str) -> None:
        self.name: str = name
        "The person's name."
        self.id: int = id
        "The person's unique identifier."
        self.choices: list[str] = choices
        "The person's event choices' names."
        self.top_choice: str = top_choice
        "The person's top_choice event name."
        return

    def __str__(self) -> str:
        return f"""Name: {self.name}; ID: {self.id}; 
Choices: {self.choices}; Top Choice: {self.top_choice}"""


def main() -> None:
    """Unit Testing"""
    person = Person(
        name="John Doe",
        id="jd0000",
        choices=["Gathering 1", "Gathering 2"],
        top_choice="Gathering 1",
    )
    print(person)
    return


if __name__ == "__main__":
    main()
