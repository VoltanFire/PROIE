import time
import sys
import hashlib
import getpass

from abc import ABC, abstractmethod
from database import get_database

class Command(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def execute(self, *args) -> None:
        pass


class INeedHelpBecayseIMayOrMayNotSuckHelpMeStepUkuIAmStuckThatIsWhyIAmHere(Command):
    name = "help"
    def execute(self, *args) -> None:
        print(f"Available commands: {', '.join([c().name for c in Command.__subclasses__()])}")


class Penis(Command):
    name = "penis"
    def execute(self, *args) -> None:
        print("penis cock 8======D")


class Logout(Command):
    name = "logout"
    def execute(self, *args) -> None:
        print("Succesfully logged out.")
        time.sleep(.75)
        sys.exit(0)


class NewUser(Command):
    name = "useradd"
    def execute(self, *args) -> None:
        username = input("Username: ")
        database = get_database()
        while username in database.keys() or " " in username:
            if username in database.keys():
                print(f"Username '{username}' is already taken.")
            elif " " in username:
                print("The username cannot contain a space.")
            username = input("Username: ")

        while (user_password := getpass.getpass(f"Password for {username}: ")) != getpass.getpass("Confirm password: "):
            print("Passwords do not match.")

        hashed_password = hashlib.sha256(user_password.encode("utf8")).hexdigest()
        database[username] = {"password": hashed_password}
        database.save()

        print(f"User '{username}' successfully created.")

