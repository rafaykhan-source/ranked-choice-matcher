"""This module is responsible for running the ranked-choice assignment script."""

import dataproducer as dp
import metrics


def main() -> None:  # noqa: C901
    """Runs the assignment script."""
    event_map = dp.get_event_map("instructors")
    options = list(event_map.values())  # all the events
    people = dp.get_people("instructors")

    # Try top choice placement
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

    # Try preferred choices placement
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

    # Try placement remaining possible options
    for person in people:
        if person.placement:
            continue

        for option_event in options:
            if not option_event.is_full():
                option_event.add_person(person)
                person.placement = option_event.name
                break

    # Print resulting assignments
    for option_event in options:
        names = []
        for person in option_event.get_roster():
            names.append(person.name)
        print(f"{option_event.name}: {names}")
        print("------------------------")

    print(metrics.get_high_satisfaction_percentage(people, event_map))
    print(metrics.get_general_satisfaction_percentage(people, event_map))
    metrics.write_results("instructors", event_map)
    print(metrics.count_unplaced(people))
    print(metrics.collect_unhappy(people))
    return


if __name__ == "__main__":
    main()
