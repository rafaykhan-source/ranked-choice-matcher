"""This module represents the Event Abstract Datatype (ADT).

Provided an event's information, the class wraps the information
and supports operations typically associated with a real-life event.

Typical usage example:

event = Event(name="Community Gathering", size_limit=15)
if not event.is_full():
    event.add_person(person)
"""

from ADTs.person import Person


class Event:
    """A simple class that wraps an event's information and supports
    event-related operations.
    """

    def __init__(self, name: str, size_limit: int) -> None:
        self.name: str = name
        "The event's name."
        self.size_limit: int = size_limit
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
            print("Error: Person cannot be added to event with full roster. ")
            return False

        self.__roster.append(person)

        return True

    def is_full(self) -> bool:
        """Returns whether the event is full.

        Returns:
            bool: Whether the event is full.
        """
        if len(self.__roster) > self.size_limit:
            print("Error: Event size limit has been exceed.")
            return True

        return len(self.__roster) == self.size_limit
