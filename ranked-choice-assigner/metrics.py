"""This module contains various metrics/evaluation functions for the assignment script.

The module's metric include high satisfaction percentage and general
satisfaction percentage.
"""

import pandas as pd
from ADTs import Event, Person


def get_high_satisfaction_percentage(
    people: list[Person],
    event_map: dict[str, Event],
) -> str:
    """Returns the high satisfaction percentage.

    The high satisfaction percentage is defined as the number of
    people that received their top choice divided by the total
    number of people.

    Args:
        people (list[Person]): People assigned events.
        event_map (dict[str, Event]): event_map with events after assignment.

    Returns:
        str: The high satisfaction metric.
    """
    top_choice_count = 0

    for person in people:
        goal_roster = event_map[person.top_choice].get_roster()
        if person in goal_roster:
            top_choice_count += 1

    return f"High Satisfaction Rating: {((top_choice_count/len(people))*100):.2f}"


def get_general_satisfaction_percentage(
    people: list[Person],
    event_map: dict[str, Event],
) -> str:
    """Returns the general satisfaction percentage.

    The general satisfaction percentage is defined as the number of
    people that received their one of their choice divided by the total
    number of people.

    Args:
        people (list[Person]): People assigned events.
        event_map (dict[str, Event]): event_map with events after assignment.

    Returns:
        str: The general satisfaction metric.
    """
    choice_count = 0

    for person in people:
        for choice in person.choices:
            roster = event_map[choice].get_roster()
            if person in roster:
                choice_count += 1
                break

    return f"General Satisfaction Rating: {((choice_count/len(people))*100):.2f}"


def write_results(csv_name: str, event_map: dict[str, Event]) -> None:
    """Writes the resulting assignments to a csv file.

    Args:
        csv_name (str): Name of csv.
        event_map (dict[str, Event]): Events
    """
    results = {}
    for event_name, event in event_map.items():
        roster = event.get_roster()
        people = [f"{person.name};{person.email}" for person in roster]
        results[event_name] = people
    df = pd.DataFrame.from_dict(results, orient="index")
    df.to_csv(f"ranked-choice-assigner/results/{csv_name}_assignments.csv")
    return


def main() -> None:
    """Unit Testing."""
    return


if __name__ == "__main__":
    main()
