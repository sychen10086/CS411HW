from typing import Any, List

class Habitat:
    def __init__(self, habitat_id: int, geographic_area: str, size: int, environment_type: str):
        self.habitat_id = habitat_id
        self.geographic_area = geographic_area
        self.size = size
        self.environment_type = environment_type
        self.animals: List[int] = []

    def update_habitat_details(self, **kwargs: dict[str, Any]) -> None:
        if "geographic_area" in kwargs:
            self.geographic_area = kwargs["geographic_area"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "environment_type" in kwargs:
            self.environment_type = kwargs["environment_type"]

    def assign_animals_to_habitat(self, animals: List[int]) -> None:
        self.animals.extend(animals)

    def get_animals_in_habitat(self) -> List[int]:
        return self.animals

    def get_habitat_details(self) -> dict:
        return {
            "habitat_id": self.habitat_id,
            "geographic_area": self.geographic_area,
            "size": self.size,
            "environment_type": self.environment_type,
            "animals": self.animals
        }
