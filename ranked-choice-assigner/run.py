"""This module is responsible for running the ranked-choice assignment script."""

import dataproducer as dp
import metrics


def main() -> None:
    """Runs the assignment script."""
    event_map = dp.get_event_map("wellness")
    options = list(event_map.values())  # all the events
    people = dp.get_people("wellness")

    for person in people:
        # Try to place person in their top choice
        if person.top_choice not in event_map:
            print(f"Error: Person's top choice not in event map - {person.top_choice}")
            break

        top_choice_event = event_map[person.top_choice]
        if not top_choice_event.is_full():
            top_choice_event.add_person(person)
            continue

        # Try to place person in one of their preferred choices
        placed = False
        choices = person.choices
        for choice in choices:
            if choice not in event_map:
                print(f"Error: Person's choice not in event map - {choice}")
                break

            choice_event = event_map[choice]
            if not choice_event.is_full():
                choice_event.add_person(person)
                placed = True
                break

        if placed:
            continue

        # Place person in one of the available options
        for option_event in options:
            if not option_event.is_full():
                option_event.add_person(person)
                break

    # Print resulting assignments
    for option_event in options:
        names = []
        for person in option_event.get_roster():
            names.append(person.name)
        print(f"{option_event.name}: {names}")
        print("------------------------")

    print(metrics.get_satisfaction_percentage(people, event_map))
    print(metrics.get_general_satisfaction_percentage(people, event_map))
    metrics.write_results("wellness", event_map)
    return


if __name__ == "__main__":
    main()
