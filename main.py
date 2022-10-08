# uku seal of approval™ :D
import hashlib
import getpass

from commands import Command
from database import get_database

while True:
    currentUser = input("Username: ")
    database = get_database()
    if currentUser in database.keys():
        testPasswd = getpass.getpass(f"Password for {currentUser}: ")
        hashTestPasswd = hashlib.sha256(testPasswd.encode("utf8")).hexdigest()

        if hashTestPasswd == database[currentUser]["password"]:
            break
        else:
            print("Incorrect password.\n")
    else:
        print("Invalid username.\n")

print(f"Logged in as '{currentUser}'.")

#main loop
while True:
    cmd = input(f"/main/{currentUser} > ").split()
    if len(cmd) == 0:
        continue

    matches = [c for c in Command.__subclasses__() if c().name == cmd[0]]
    if len(matches) == 0:
        print("No command found? :nobitches: heheheha your mom")
    else:
        matches[0]().execute(*cmd[1:])
