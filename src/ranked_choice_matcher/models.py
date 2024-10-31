"""This module contains the models for the program."""

from copy import deepcopy
from dataclasses import dataclass, field


@dataclass(slots=True)
class Person:
    """Wraps the information associated with a person."""

    name: str
    email: str
    choices: list[str]
    top_choice: str
    placement: str = ""


@dataclass(slots=True)
class Event:
    """A class wrapping an event's information and containing event-related operations.

    Attributes:
        name (str): The event's name.
        capacity (int): The event's size limit.
    """

    name: str
    capacity: int
    "The occupancy limit for the event."
    roster: list[Person] = field(default_factory=list)
    "The current event roster."

    def add_person(self, person: Person) -> bool:
        """Adds a person to the event roster.

        Args:
            person (Person): Person to add to roster.

        Returns:
            bool: Whether person was successfully added to event.
        """
        if self.is_full():
            print("Error: Person cannot be added to event with full roster.")
            return False

        self.roster.append(person)

        return True

    def is_full(self) -> bool:
        """Returns whether the event is full.

        Returns:
            bool: Whether the event is full.
        """
        if len(self.roster) > self.capacity:
            print("Error: Event capacity has been exceed.")
            return True

        return len(self.roster) == self.capacity

    def get_roster(self) -> list[Person]:
        """Returns a shallow copy of the event roster.

        Returns:
            list[Person]: The event's roster.
        """
        return self.roster.copy()

    def get_roster_deep(self) -> list[Person]:
        """Returns a deep copy of the event roster.

        Returns:
            list[Person]: The event's roster.
        """
        return deepcopy(self.roster)

    def __str__(self) -> str:
        """Returns string representation of the event.

        Returns:
            str: Event's information.
        """
        return f"""Name: {self.name}
Capacity: {self.capacity}
Roster: {self.roster}"""


if __name__ == "__main__":
    pass
