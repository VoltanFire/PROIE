import json
from pathlib import Path

DATABASE_FILE = "database.json"


class Database(dict):
    def __init__(self, jsonn):
        super().__init__(jsonn)

    def save(self):
        with open(DATABASE_FILE, "w+") as db_file:
            json.dump(self, db_file, indent=2)


DEFAULT_DATABASE = Database({
    "root": {
        "password": "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
    }  # default password is 'admin'
})


def get_database() -> Database:
    if not Path(DATABASE_FILE).is_file():  # Create file if not already on da computer
        DEFAULT_DATABASE.save()
        return DEFAULT_DATABASE

    with open(DATABASE_FILE, "r") as db_file:
        return Database(json.load(db_file))
