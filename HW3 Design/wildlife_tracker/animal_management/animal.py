from typing import Any, Optional

class Animal:
    def __init__(self, animal_id: int, species: str, age: Optional[int] = None):
        self.animal_id = animal_id
        self.species = species
        self.age = age

    def get_details(self) -> dict[str, Any]:
        # Method to get details about the animal
        return {
            "animal_id": self.animal_id,
            "species": self.species,
            "age": self.age
        }

    def update_details(self, **kwargs: Any) -> None:
        if "species" in kwargs:
            self.species = kwargs["species"]
        if "age" in kwargs:
            self.age = kwargs["age"]
