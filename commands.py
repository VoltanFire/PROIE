import getpass
import hashlib
import sys
import time
from abc import ABC, abstractmethod
from argparse import ArgumentParser, Namespace

import proie
from database import get_database


class Command(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    def update_parser(self, parser: ArgumentParser) -> None:
        pass

    @abstractmethod
    def execute(self, args: Namespace) -> None:
        pass

#INeedHelpBecauseIMayOrMayNotSuckHelpMeStepUkuIAmStuckThatIsWhyIAmHere
class Hilfe(Command):
    name = "help"

    def execute(self, args: Namespace) -> None:
        print(f"Available commands: {', '.join([c().name for c in Command.__subclasses__()])}")
        # TODO 'help command' returns helps about a specific command


class Penis(Command):
    name = "penis"

    def update_parser(self, parser: ArgumentParser) -> None:
        parser.add_argument("--cock", '-c', type=int)

    def execute(self, args: Namespace) -> None:
        if args.cock is None:
            print("smol penis ? :nobitches: :-) (smol penis not smiley)")
            return
        try:
            print(f"penis cock 8{'='*args.cock}D")
        except ValueError:
            print("you didnt put a lenght hehehaha")


class Logout(Command):
    name = "logout"

    def execute(self, args: Namespace) -> None:
        proie.current_user = None
        print("Successfully logged out.\n")


class Shutdown(Command):
    name = "shutdown"

    def execute(self, args: Namespace) -> None:
        print("Shutting down...")
        time.sleep(.75)
        sys.exit()


class NewUser(Command):
    name = "useradd"

    def update_parser(self, parser: ArgumentParser) -> None:
        parser.add_argument("username")
        parser.add_argument('--superuser', '-s', action="store_true")

    def execute(self, args: Namespace) -> None:
        if args.username is None:
            print("You need to specify an username.")
            return
        elif (username := args.username) in (database := get_database()).keys():
            print(f"Username '{username}' is already taken.")
            return
        elif args.superuser and not database[proie.current_user]["superuser"]:
            print("You don't have enough permissions to create a superuser account.")
            return

        while (user_password := getpass.getpass(f"Password for {username}: ")) != getpass.getpass("Confirm password: "):
            print("Passwords do not match.")

        if args.superuser and user_password.strip() == "":
            print("Superusers can't have empty passwords.")
            return

        hashed_password = hashlib.sha256(user_password.encode("utf8")).hexdigest()
        database[username] = {"password": hashed_password, "superuser": args.superuser}
        database.save()

        print(f"User '{username}' successfully created.")
