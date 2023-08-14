"""This module contains various metrics/evaluation functions for
for assignment script."""

from ADTs import Event, Person


def get_satisfaction_percentage(
    people: list[Person], event_map: dict[str, Event]
) -> str:
    """Returns the satisfaction percentage.

    The satisfaction percentage is defined as the number of
    people that received their top choice divided by the total
    number of people.

    Args:
        people (list[Person]): People assigned events.
        events (dict[str, Event]): event_map with events after assignment.

    Returns:
        str: The satisfaction metric.
    """
    top_choice_count = 0

    for person in people:
        goal_roster = event_map[person.top_choice].get_roster()
        if person in goal_roster:
            top_choice_count += 1

    return f"Satisfaction Rating: {(top_choice_count/len(people))*100}"
