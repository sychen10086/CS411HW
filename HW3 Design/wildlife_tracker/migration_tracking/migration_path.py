class MigrationPath:
    def __init__(self, path_id: int, species: str, start_habitat: Habitat, end_habitat: Habitat, duration: int):
        self.path_id = path_id
        self.species = species
        self.start_habitat = start_habitat
        self.end_habitat = end_habitat
        self.duration = duration

    def get_path_details(self) -> dict:
        return {
            "path_id": self.path_id,
            "species": self.species,
            "start_habitat": self.start_habitat.get_habitat_details(),
            "end_habitat": self.end_habitat.get_habitat_details(),
            "duration": self.duration,
        }

    def update_path_details(self, **kwargs: Any) -> None:
        if "species" in kwargs:
            self.species = kwargs["species"]
        if "start_habitat" in kwargs:
            self.start_habitat = kwargs["start_habitat"]
        if "end_habitat" in kwargs:
            self.end_habitat = kwargs["end_habitat"]
        if "duration" in kwargs:
            self.duration = kwargs["duration"]
