"""This module is responsible for running the ranked-choice assignment script."""

import dataproducer as dp


def main() -> None:
    event_map = dp.get_event_map()
    people = dp.get_people()

    for person in people:
        if person.top_choice not in event_map:
            print(f"Error: Person's top choice not in event map - {person.top_choice}")
            break

        top_choice_event = event_map[person.top_choice]
        if not top_choice_event.is_full():
            top_choice_event.add_person(person)
            continue

        choices = person.choices
        for choice in choices:
            if choice not in event_map:
                print(f"Error: Person's choice not in event map - {choice}")
                break

            choice_event = event_map[choice]
            if not choice_event.is_full():
                choice_event.add_person(person)

    for event in event_map.values():
        print(event.name, event.get_roster())

    return


if __name__ == "__main__":
    main()
