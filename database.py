import json
from pathlib import Path

class Database(dict):
    def __init__(self, jsonn):
        super().__init__(jsonn)

    def save(self):
        with open("database.json", "w+") as db_file:
            json.dump(self, db_file, indent=2)

_DEFAULT_DATABASE = Database({
    "admin": {
        "password": "4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2"
    } # default password is 'root'
})

def get_database() -> Database:
    if not Path("database.json").is_file(): # Create file if not already on da computer
        _DEFAULT_DATABASE.save()
        return _DEFAULT_DATABASE

    with open("database.json", "r") as db_file:
        return Database(json.load(db_file))