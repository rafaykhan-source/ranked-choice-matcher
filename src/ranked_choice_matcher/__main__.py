"""This module is responsible for running the ranked-choice matching script."""

import argparse

import metrics

from ranked_choice_matcher.dataserver import DataServer
from ranked_choice_matcher.datawriter import DataWriter


def get_parsed_arguments() -> argparse.Namespace:
    """Returns parsed arguments.

    Returns:
        argparse.ArgumentParser: The argument parser.
    """
    parser = argparse.ArgumentParser(
        prog="Ranked Choice Matcher",
        description="Matches people to sections based on their ranked preferences.",
        epilog="See datapipelines for data format.",
    )
    parser.add_argument(
        "GROUP",
        help="a group to run ranked-choice-matcher on",
    )
    return parser.parse_args()


def main() -> None:  # noqa
    """Runs the matching script."""
    args = get_parsed_arguments()
    d = DataServer()
    event_map = d.get_events(f"data/events/{args.GROUP}.csv")
    print(event_map)
    options = list(event_map.values())
    people = d.get_people(f"data/groups/{args.GROUP}.csv")

    # Pre-Determined Placements
    for person in people:
        if not person.placement:
            continue

        if person.placement not in event_map:
            print(
                f"Error: Person's pre-determined placement not in event map - {person.placement}"  # noqa
            )
            continue

        placement_event = event_map[person.placement]
        if not placement_event.is_full():
            placement_event.add_person(person)
            person.placement = placement_event.name
            continue

    # Top-Choice Placements
    for person in people:
        if person.placement:
            continue

        if person.top_choice not in event_map:
            print(f"Error: Person's top choice not in event map - {person.top_choice}")
            continue

        top_choice_event = event_map[person.top_choice]
        if not top_choice_event.is_full():
            top_choice_event.add_person(person)
            person.placement = top_choice_event.name
            continue

    # Preferred Choice Placements
    for person in people:
        if person.placement:
            continue

        choices = person.choices
        for choice in choices:
            if choice not in event_map:
                print(f"Error: Person's choice not in event map - {choice}")
                continue

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

    # Show Events
    for option_event in options:
        names = [person.name for person in option_event.get_roster()]
        print(f"{option_event.name}: {names}")
        print("------------------------")

    print(metrics.get_high_satisfaction_percentage(people, event_map))
    print(metrics.get_general_satisfaction_percentage(people, event_map))
    r = DataWriter()
    r.write_results(f"results/{args.GROUP}.csv", people)
    print(metrics.count_unplaced(people))
    print("\n".join([str(p) for p in metrics.collect_unhappy(people)]))


main()