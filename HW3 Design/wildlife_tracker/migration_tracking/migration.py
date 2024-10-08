class Migration:
    def __init__(self, migration_id: int, species: str, start_location: Habitat, destination: Habitat):
        self.migration_id = migration_id
        self.species = species
        self.start_location = start_location
        self.destination = destination

    def get_migration_details(self) -> dict:
        return {
            "migration_id": self.migration_id,
            "species": self.species,
            "start_location": self.start_location.get_habitat_details(),
            "destination": self.destination.get_habitat_details(),
        }

    def update_migration_details(self, **kwargs: Any) -> None:
        if "species" in kwargs:
            self.species = kwargs["species"]
        if "start_location" in kwargs:
            self.start_location = kwargs["start_location"]
        if "destination" in kwargs:
            self.destination = kwargs["destination"]
