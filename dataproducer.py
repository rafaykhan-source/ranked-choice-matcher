"""This module represents the data producer for the project."""

from ADTs import Event, Person


def get_event_map() -> dict[str, Event]:
    """Returns a mapping of event name strings to event objects.

    Returns:
        dict[str, Event]: event map
    """

    mapping = {
        "Gathering 1": Event(name="Gathering 1", capacity=1),
        "Gathering 2": Event(name="Gathering 2", capacity=0),
        "Gathering 3": Event(name="Gathering 3", capacity=0),
        "Gathering 4": Event(name="Gathering 4", capacity=3),
    }

    return mapping


def get_people() -> list[Person]:
    """Returns people who must be listed on an event.

    Returns:
        list[Person]: people who must be listed on an event.
    """
    people = [
        Person(
            name="John Doe",
            id="jd0000",
            choices=["Gathering 1", "Gathering 2"],
            top_choice="Gathering 1",
        ),
        Person(
            name="Jane Doe",
            id="jd0000",
            choices=["Gathering 1", "Gathering 3"],
            top_choice="Gathering 1",
        ),
    ]

    return people
