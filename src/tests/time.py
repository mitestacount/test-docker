import time
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=False, slots=True)
class PersonSlots:
    name = "John Doe s"
    birthdate = datetime(2000, 1, 1)


class PersonwithStr:
    __slots__ = ["name", "birthdate"]

    def __init__(self, name="John Doe", birthdate=datetime(2000, 1, 1)):
        self.name = name
        self.birthdate = birthdate


# dataclass of person
@dataclass(frozen=False, slots=False)
class Person:
    name: str = "John Doe"
    birthdate: datetime = datetime(2000, 1, 1)


def print_with_time(text: Person | PersonSlots | PersonwithStr):
    start = time.time()
    name = text.name
    text.name = "New Name"
    end = time.time()
    time_exec = end - start
    print(f"Time: {time_exec*1000000} of {name} {text=}")


"""gaa = PersonwithStr()
slots_man = PersonSlots()
without_slot = Person()
print_with_time(slots_man)
print_with_time(without_slot)
print_with_time(without_slot)
"""


class Thing:
    var: int = 1
    number: str = "variable"

    def __init__(self, name: str):
        self.name = name


@dataclass
class Thing2:
    name: str
    var: int = 1
    number: str = "variable"


Thing2("name")
Thing("name")
