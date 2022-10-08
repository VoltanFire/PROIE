# uku seal of approval™ :D

import hashlib
import getpass

from commands import Command #FIXME circular import

file = "database"
#FIXME create database if not here (later maybe)

#creating dictionary user->passwd and keeping track of users in the file
database = {}
user_list = [] #FIXME different file for user list

#read the file and fill the dictionary
with open(file, "r") as ofp:
    for line in ofp:
        user,passwd = line.split("@")
        database[user] = passwd.replace("\n", "")
        user_list.append(user)

#creating a list or easier UX
registeredUser = "Registered users |"
for user in user_list :
     registeredUser += user+"|"

#^^^^^^^^^^^^^^^^^^^am satisfied until there^^^^^^^^^^^^^^^^^^^

#registering needs to be redone (or not)
while True:
    print(f"\n{registeredUser}")
    currentUser = input("Username \n> ")
    if currentUser in database:
        testPasswd = getpass.getpass(f"Password for {currentUser} \n> ")
        hashTestPasswd = hashlib.sha256(testPasswd.encode("utf8")).hexdigest()

        if hashTestPasswd == database[currentUser]:
            break
        else:
            print("Incorrect password, back to username")
    else:
        print("Invalid username")

del database


print(f"Logged in as {currentUser}")

#-------------------------Main code----------------------------
#TODO trying object oriented commands for a better mainloop (am doing that curently)
#TODO Filesystem, filemanagment

#main loop
while True:
    cmd = input(f"\main\\{currentUser} > ")
    matches = [c for c in Command.__subclasses__() if c().name == cmd]
    if len(matches) == 0:
        print("No command found? :nobitches: heheheha your mom")
    else:
        matches[0]().execute() # TODO args
