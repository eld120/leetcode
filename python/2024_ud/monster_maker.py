"""

Tasks

We are going to design some classes and functions to create and interact with `Monster`s. 
The below descriptions are using generic pseudocode — the class and function signatures will look different in the specific programming language you are using.

The class and function definitions below are not fully specified — you will need to make some 
decisions about how they should work to be useful to someone who would use your code in their own projects.

Please implement the following:

- An `Animal` class
    - Example constructor call: `Animal(name: "Octopus", numLegs: 8, sound: "Burble")`
- A `Monster` class, that creates a `Monster` from an `Animal` head and an `Animal` body
    - Example constructor call: `Monster(head: Animal(Octopus), body: Animal(Scorpion))`
        - `Monster.name` → `OctopusScorpion`
        - `Monster.sound` → `BurbleHiss` 
    - Your code should ensure that we can only create a `Monster` with the head and body of two different `Animals`, who have the same number of legs.
- A function `createAllMonsters` that takes as input a number of legs and returns an array of all `Monsters` that can be made with that number of legs. A `Monster` with `Animal` A head and `Animal` B body is distinct from a `Monster` with `Animal` B head and `Animal` A body. Please use the animals.txt file linked at the beginning of this problem.
    - Example function call: `createAllMonsters(8)` → `[Monster(OctopusScorpion), Monster(ScorpionOctopus)]`
    - The crux of this function is: how do we produce all of the combinations of heads and bodies for animals with a given number of legs?
- A function `getRandomMonster` that takes as input a number of legs and returns a random Monster with that number of legs.
    - Example function call: `getRandomMonster(8)` → `Monster(OctopusScorpion)`
    - This function should call your `createAllMonsters` function
"""
import random
from csv import DictReader
from typing import List


class Animal:
    def __init__(self, name: str, legs: int, sound: str) -> None:
        self.name = name
        self.legs = legs
        self.sound = sound

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return self.__str__()


class Monster:
    def __init__(self, head: Animal, body: Animal) -> None:
        if head.legs != body.legs:
            raise RuntimeError("MUST HAVE THE SAME NUMBER OF LEGS")
        self.head = head
        self.body = body
        self.name = f"{head}{body}"
        self.sound = f"{head}{body}"
        self.legs = self.head.legs

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, __value: object) -> bool:
        return self.__str__() == __value.__str__()


def create_all_monsters(legs: int) -> List:
    with open("./animals.csv", "r") as f:
        # AnimalName,AnimalType,NumLegs,Sound
        reader = DictReader(f)
        all_animals = []
        for line in reader:
            if int(line["NumLegs"]) == legs:
                all_animals.append(
                    Animal(line["AnimalName"], int(line["NumLegs"]), line["Sound"])
                )
        all_monsters = []
        for animal in all_animals:
            for a in all_animals:
                if animal != a:
                    all_monsters.append(Monster(animal, a))
        return all_monsters


def get_random_monster(legs: int) -> Monster:
    monsters = create_all_monsters(legs)

    r = random.randint(0, len(monsters) - 1)
    return monsters[r]


if __name__ == "__main__":
    print(create_all_monsters(4))
    print(get_random_monster(4))
