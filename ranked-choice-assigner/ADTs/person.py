"""This module contains the Person Abstract Datatype (ADT).

This class wraps typical spreadsheet information
associated with a person for the ranked-choice assignment
task.

Typical usage example:

person = Person(
    name="John Doe",
    email="jd0000@123mail.com",
    choices=["choice_1", "choice_2", "choice_3"],
    top_choice="choice_1",
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
        placement: str = "",
    ) -> None:
        """Instantiates the person class.

        Args:
            name (str): Person's name.
            email (str): Person's unique email.
            choices (list[str]): Person's event choices.
            top_choice (str): Person's top event choice.
            placement (str, optional): Person's placement (if known). Defaults to "".
        """
        self.name: str = name
        "The person's name. Instance Variable."
        self.email: int = email
        "The person's unique identifier/email. Instance Variable."
        self.choices: list[str] = choices
        "The person's event choices' names. Instance Variable."
        self.top_choice: str = top_choice
        "The person's top_choice event name. Instance Variable."
        self.placement: str = placement
        "The person's placed event name. Instance Variable."
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
