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
    "admin": {
        "password": "4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2"
    }  # default password is 'root'
})


def get_database() -> Database:
    if not Path(DATABASE_FILE).is_file():  # Create file if not already on da computer
        DEFAULT_DATABASE.save()
        return DEFAULT_DATABASE

    with open(DATABASE_FILE, "r") as db_file:
        return Database(json.load(db_file))
