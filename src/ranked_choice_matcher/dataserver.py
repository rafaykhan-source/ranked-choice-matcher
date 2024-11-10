"""This module represents the data server for the project.

It is responsible for loading data pertaining to the matching task and mapping this
data to custom ADTs.
"""

import csv
import random
from dataclasses import dataclass

from ranked_choice_matcher.models import Event, Person


@dataclass
class DataServer:
    """This class is responsible for data retrieval."""

    def get_people(self, file_path: str) -> list[Person]:
        """Returns the people at file_path.

        Args:
            file_path (str): The file path.

        Returns:
            list[Person]: The people at file_path.
        """
        with open(file_path) as csv_file:
            reader = csv.DictReader(csv_file)
            people = [
                Person(
                    row["name"],
                    row["email"],
                    row["choices"].split(","),
                    row["top_choice"],
                    row["placement"],
                )
                for row in reader
            ]
            random.shuffle(people)
            return people

    def get_events(self, file_path: str) -> dict[str, Event]:
        """Returns the events at file_path.

        Args:
            file_path (str): The file path.

        Returns:
            dict[str, Event]: The mapping of event names to events.
        """
        with open(file_path) as csv_file:
            reader = csv.DictReader(csv_file)
            return {
                row["name"]: Event(row["name"], int(row["capacity"])) for row in reader
            }


if __name__ == "__main__":
    pass
