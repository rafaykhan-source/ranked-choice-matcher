"""This represents the placement strategies for the program."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from ranked_choice_matcher.models import Event, Person


class PlacementStrategy(ABC):
    """This represents a strategy for placing people."""

    @abstractmethod
    def set_placements(self, people: list[Person], event_map: dict[str, Event]) -> None:
        """Sets people's placements to events."""


@dataclass
class NaiveTopChoiceStrategy(PlacementStrategy):
    """Places people into their favorite available choice if there is space."""

    def set_placements(self, people: list[Person], event_map: dict[str, Event]) -> None:
        """Sets people's placements to events.

        Args:
            people (list[Person]): The people to place.
            event_map (dict[str, Event]): The mapping of event names to events.
        """
        options = list(event_map.values())
        # Pre-Determined Placements
        for person in people:
            if not person.placement:
                continue

            placement_event = event_map[person.placement]
            if not placement_event.is_full():
                placement_event.add_person(person)
                person.placement = placement_event.name
                continue

        # Top-Choice Placements
        for person in people:
            top_choice_event = event_map[person.top_choice]
            if not top_choice_event.is_full():
                top_choice_event.add_person(person)
                person.placement = top_choice_event.name
                continue

        # Preferred Choice Placements
        for person in people:
            for choice in person.choices:
                choice_event = event_map[choice]
                if not choice_event.is_full():
                    choice_event.add_person(person)
                    person.placement = choice_event.name
                    break

        # Remaining Placements
        for person in people:
            if person.placement:
                continue

            for option_event in options:
                if not option_event.is_full():
                    option_event.add_person(person)
                    person.placement = option_event.name
                    break
