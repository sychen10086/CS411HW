class MigrationManager:
    def __init__(self):
        self.migrations: dict[int, Migration] = {}

    def schedule_migration(self, migration: Migration) -> None:
        self.migrations[migration.migration_id] = migration

    def cancel_migration(self, migration_id: int) -> None:
        if migration_id in self.migrations:
            del self.migrations[migration_id]

    def get_migration_by_id(self, migration_id: int) -> Optional[Migration]:
        return self.migrations.get(migration_id)
