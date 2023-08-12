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
        self.__attendees: list[Person] = []
        return
