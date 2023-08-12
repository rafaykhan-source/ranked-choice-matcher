"""This module represents the Event Abstract Datatype (ADT).

Provided an event's information, the class wraps the information
and supports operations typically associated with a real-life event.

Typical usage example:

event = Event(name="Community Gathering", size_limit=15)
if not event.is_full():
    event.add_person(person)
"""