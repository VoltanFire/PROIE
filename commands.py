import getpass
import hashlib
import sys
import time
from abc import ABC, abstractmethod

import proie
from database import get_database


class Command(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def execute(self, *args) -> None:
        pass


class INeedHelpBecauseIMayOrMayNotSuckHelpMeStepUkuIAmStuckThatIsWhyIAmHere(Command):
    name = "help"

    def execute(self, *args) -> None:
        print(f"Available commands: {', '.join([c().name for c in Command.__subclasses__()])}")


class Penis(Command):
    name = "penis"

    def execute(self, *args) -> None:
        if len(args) == 0:
            print("smol penis ? :nobitches: :-) (smol penis not smiley)")
            return
        try : print(f"penis cock 8{'='*int(args[0])}D")
        except ValueError: print("you didnt put a lenght hehehaha")


class Logout(Command):
    name = "logout"

    def execute(self, *args) -> None:
        proie.current_user = None
        print("Successfully logged out.\n")


class Shutdown(Command):
    name = "shutdown"

    def execute(self, *args) -> None:
        print("Shutting down...")
        time.sleep(.75)
        sys.exit()


class NewUser(Command):
    name = "useradd"

    def execute(self, *args) -> None:
        if len(args) == 0:
            print("You need to specify an username.")
            return
        elif (username := args[0]) in (database := get_database()).keys():
            print(f"Username '{username}' is already taken.")
            return

        while (user_password := getpass.getpass(f"Password for {username}: ")) != getpass.getpass("Confirm password: "):
            print("Passwords do not match.")

        hashed_password = hashlib.sha256(user_password.encode("utf8")).hexdigest()
        database[username] = {"password": hashed_password}
        database.save()

        print(f"User '{username}' successfully created.")
