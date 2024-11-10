"""The datawriter for the matching program."""

import csv
from dataclasses import dataclass

from ranked_choice_matcher.models import Person


@dataclass
class DataWriter:
    """This class is responsible for writing results."""

    def write_results(self, file_path: str, people: list[Person]) -> None:
        """Writes the resulting assignments to a csv file.

        Args:
            file_path (str): The file path.
            people (list[Person]): The people to write.
        """
        with open(file_path, "w", newline="") as csv_file:
            fields = ["name", "email", "placement"]
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writeheader()

            for person in people:
                writer.writerow(
                    {
                        "name": person.name,
                        "email": person.email,
                        "placement": person.placement,
                    },
                )
