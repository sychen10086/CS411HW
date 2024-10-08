from typing import Optional

class AnimalManager:
    def __init__(self) -> None:
        self.animals: dict[int, Animal] = {}

    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        return self.animals.get(animal_id, None)

    def register_animal(self, animal: Animal) -> None:
        self.animals[animal.animal_id] = animal

    def remove_animal(self, animal_id: int) -> None:
        if animal_id in self.animals:
            del self.animals[animal_id]

