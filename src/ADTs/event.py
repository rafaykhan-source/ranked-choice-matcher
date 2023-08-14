"""This module represents the Event Abstract Datatype (ADT).

Provided an event's information, the class wraps the information
and supports operations typically associated with a real-life event.

Typical usage example:

event = Event(name="Community Gathering", capacity=15)
if not event.is_full():
    event.add_person(person)
"""

from ADTs.person import Person
from copy import deepcopy


class Event:
    """A class wrapping an event's information and supporting
    event-related operations.
    """

    def __init__(self, name: str, capacity: int) -> None:
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
        return f"Name: {self.name}; Capacity: {self.capacity}; Roster: {self.__roster}"


def main() -> None:
    """Unit Testing."""
    event = Event(name="Gathering 1", capacity="2")
    print(event)
    return


if __name__ == "__main__":
    main()
