"""This module contains various utility functions for the ranked choice matcher program."""

from ranked_choice_matcher.models import Event, Person


def validate_options(people: list[Person], event_map: dict[str, Event]) -> None:
    """Validates that the people's options are events.

    Args:
        people: The people whose choices to validate.
        event_map: The events.
    """
    for person in people:
        if person.placement and person.placement not in event_map:
            print(
                f"Error: Person's pre-determined placement not in event map - {person.placement}",
            )
            continue

        if person.top_choice not in event_map:
            print(
                f"Error: Person's top choice not in event map - {person.top_choice}",
            )

        for choice in person.choices:
            if choice not in event_map:
                print(f"Error: Person's choice not in event map - {choice}")
