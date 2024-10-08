from typing import Optional, List

class HabitatManager:
    def __init__(self):
        self.habitats: dict[int, Habitat] = {}

    def get_habitat_by_id(self, habitat_id: int) -> Optional[Habitat]:
        return self.habitats.get(habitat_id)

    def create_habitat(self, habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        habitat = Habitat(habitat_id, geographic_area, size, environment_type)
        self.habitats[habitat_id] = habitat
        return habitat

    def remove_habitat(self, habitat_id: int) -> None:
        if habitat_id in self.habitats:
            del self.habitats[habitat_id]
