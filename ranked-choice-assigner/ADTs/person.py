"""This module contains the Person Abstract Datatype (ADT).

Provided a Person's information from a spreadsheet, this class
functions primarily as a wrapper of one's information, their
ranked choices and supports operations.

Typical usage example:

person = Person(name="John Doe",
                email="jd0000@123mail.com",
                choices=["choice1", "choice2", "choice3"],
                top_choice="choice1",
                )
"""


class Person:
    """A class wrapping a person's information."""

    def __init__(
        self,
        name: str,
        email: str,
        choices: list[str],
        top_choice: str,
    ) -> None:
        """Instantiates the person class.

        Args:
            name (str): Person's name.
            email (str): Person's unique email.
            choices (list[str]): Person's event choices.
            top_choice (str): Person's top event choice.
        """
        self.name: str = name
        "The person's name."
        self.email: int = email
        "The person's unique identifier/email."
        self.choices: list[str] = choices
        "The person's event choices' names."
        self.top_choice: str = top_choice
        "The person's top_choice event name."
        return

    def __str__(self) -> str:
        """Returns a string representation of the person.

        Returns:
            str: Person's information.
        """
        return f"""Name: {self.name}; ID: {self.email};
Choices: {self.choices}; Top Choice: {self.top_choice}"""


def main() -> None:
    """Unit Testing."""
    person = Person(
        name="John Doe",
        email="jd0000",
        choices=["Gathering 1", "Gathering 2"],
        top_choice="Gathering 1",
    )
    print(person)
    return


if __name__ == "__main__":
    main()
