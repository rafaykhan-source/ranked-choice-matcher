"""This module is responsible for running the ranked-choice matching script."""

import argparse

from ranked_choice_matcher import metrics
from ranked_choice_matcher.dataserver import DataServer
from ranked_choice_matcher.datawriter import DataWriter
from ranked_choice_matcher.strategies import NaiveTopChoiceStrategy
from ranked_choice_matcher.utility import validate_options


def get_args() -> argparse.Namespace:
    """Returns arguments.

    Returns:
        argparse.Namespace: The parsed arguments.
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
    args = get_args()

    d = DataServer()
    event_map = d.get_events(f"data/events/{args.GROUP}.csv")
    options = list(event_map.values())
    people = d.get_people(f"data/groups/{args.GROUP}.csv")
    validate_options(people, event_map)

    NaiveTopChoiceStrategy().set_placements(people, event_map)

    metrics.show_placements(options)
    print(metrics.get_high_satisfaction_percentage(people, event_map))
    print(metrics.get_general_satisfaction_percentage(people, event_map))
    print(metrics.count_unplaced(people))
    print("\n".join([str(p) for p in metrics.collect_unhappy(people)]))

    r = DataWriter()
    r.write_results(f"results/{args.GROUP}.csv", people)


main()
