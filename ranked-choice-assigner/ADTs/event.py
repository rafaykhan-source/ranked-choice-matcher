"""This module represents the Event Abstract Datatype (ADT).

This class wraps the information and supports operations
associated with a real-life event.

Typical usage example:

event = Event(name="Community Gathering", capacity=15)
if not event.is_full():
    event.add_person(person)
"""

from copy import deepcopy

from ADTs.person import Person


class Event:
    """A class wrapping an event's information and containing event-related operations.

    Attributes:
        name (str): The event's name.
        capacity (int): The event's size limit.
    """

    def __init__(self, name: str, capacity: int) -> None:
        """Instantiates an event.

        Args:
            name (str): Name of the event.
            capacity (int): Event's size limit.
        """
        self.name: str = name
        "The event's name."
        self.capacity: int = capacity
        "The occupancy limit for the event."
        self.__roster: list[Person] = []
        "The current event roster."
        return

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

        self.__roster.append(person)

        return True

    def is_full(self) -> bool:
        """Returns whether the event is full.

        Returns:
            bool: Whether the event is full.
        """
        if len(self.__roster) > self.capacity:
            print("Error: Event capacity has been exceed.")
            return True

        return len(self.__roster) == self.capacity

    def get_roster(self) -> list[Person]:
        """Returns a shallow copy of the event roster.

        Returns:
            list[Person]: The event's roster.
        """
        return self.__roster.copy()

    def get_roster_deep(self) -> list[Person]:
        """Returns a deep copy of the event roster.

        Returns:
            list[Person]: The event's roster.
        """
        return deepcopy(self.__roster)

    def __str__(self) -> str:
        """Returns string representation of the event.

        Returns:
            str: Event's information.
        """
        return f"Name: {self.name}; Capacity: {self.capacity}; Roster: {self.__roster}"


def main() -> None:
    """Unit Testing."""
    event = Event(name="Gathering 1", capacity="2")
    print(event)
    return


if __name__ == "__main__":
    main()
