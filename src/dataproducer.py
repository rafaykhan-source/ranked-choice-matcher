"""This module represents the data producer for the project.

It is responsible for loading data pertaining to the
ranked-choice assignment task and mapping this data to
custom ADTs.
"""

import pandas as pd
from adt import Event, Person


def get_event_map(group_type: str) -> dict[str, Event]:
    """Returns a mapping of event name strings to event objects.

    Returns:
        dict[str, Event]: event map
    """
    if group_type == "wellness":
        data = __load_data("wellness_events.csv")
    else:
        data = __load_data("community_events.csv")
    events = list(map(__create_event, data.values.tolist()))

    event_map = {}
    for event in events:
        event_map[event.name] = event

    return event_map


def __load_data(csv_name: str) -> pd.DataFrame:
    """Loads data from csv with specified name.

    Args:
        csv_name (str): Name of the csv for data retrieval.

    Returns:
        pd.DataFrame: data
    """
    return pd.read_csv(f"processed-data/{csv_name}")


def __create_event(row: list) -> Event:
    return Event(
        name=row[0].strip(),
        capacity=row[1],
    )


def __create_person(row: list) -> Person:
    return Person(
        name=row[1],
        email=row[0].strip(),
        choices=row[2].split(","),
        top_choice=row[3],
    )


def get_people(group_type: str) -> list[Person]:
    """Returns a list of Person objects.

    Returns:
        list[Person]: people in group
    """
    if group_type == "wellness":
        data = __load_data("wellness.csv")
    else:
        data = __load_data("community.csv")

    return list(map(__create_person, data.values.tolist()))


def main() -> None:
    """Unit Testing."""
    people = get_people("wellness")

    for person in people:
        print(person)
        print("------------")
    return


if __name__ == "__main__":
    main()
