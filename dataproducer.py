"""This module represents the data producer for the project."""

from ADTs import Event, Person


def get_event_map() -> dict[str, Event]:
    """Returns a mapping of event name strings to event objects.

    Returns:
        dict[str, Event]: event map
    """

    mapping = {
        "Gathering 1": Event(name="Gathering 1", capacity="2"),
        "Gathering 2": Event(name="Gathering 2", capacity="3"),
        "Gathering 3": Event(name="Gathering 3", capacity="2"),
        "Gathering 4": Event(name="Gathering 4", capacity="3"),
    }

    return mapping


def get_people() -> list[Person]:
    """Returns people who must be listed on an event.

    Returns:
        list[Person]: people who must be listed on an event.
    """
    people = []

    return people
