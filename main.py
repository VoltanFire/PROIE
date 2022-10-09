# PROIE is a P.R.O.I.E. Inc. property, all rights reserved.
# uku seal of approval™ :D
# cambouis seal of approval too ;)
import sys
from argparse import ArgumentParser
from getpass import getpass
from hashlib import sha256

import proie
from commands import Command, Hilfe
from database import get_database


def login() -> str:
    database = get_database()
    while True:
        while (user_input := input("Username: ")) not in database.keys():
            print("Invalid username.\n")

        password_input = sha256(getpass(f"Password for {user_input}: ").encode("utf8")).hexdigest()
        if password_input != database[user_input]["password"]:
            print("Incorrect password.\n")
        else:
            print(f"Logged in as '{user_input}'.")
            return user_input


# main loop
while True:
    if proie.current_user is None:
        proie.current_user = login()

    cmd = input(f"/main/{proie.current_user} > ").split()
    if len(cmd) == 0:
        continue

    matches = [c for c in Command.__subclasses__() if c().name == cmd[0]]
    if len(matches) == 0:
        matches = [Hilfe]

    command = matches[0]()
    parser = ArgumentParser(prog=command.name)

    command.update_parser(parser)
    try:
        command.execute(parser.parse_args(cmd[1:]))
    except SystemExit:  # hehehehehehehe
        if command.name == "shutdown":
            sys.exit()
