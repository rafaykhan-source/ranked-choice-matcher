"""This module is responsible for running the ranked-choice matching script."""

import argparse

import metrics

from ranked_choice_matcher.dataserver import DataServer
from ranked_choice_matcher.datawriter import DataWriter
from ranked_choice_matcher.strategies import NaiveTopChoiceStrategy


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


def main() -> None:
    """Runs the matching script."""
    args = get_parsed_arguments()
    d = DataServer()
    event_map = d.get_events(f"data/events/{args.GROUP}.csv")
    print(event_map)
    options = list(event_map.values())
    people = d.get_people(f"data/groups/{args.GROUP}.csv")

    NaiveTopChoiceStrategy().set_placements(people, event_map)

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
