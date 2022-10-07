from cryptage import crypt

import getpass
import time
import sys


crypted = "c_database"
uncrypted = "database"

key = "SuperVoltan69"

crypt(crypted,uncrypted,key)

#creating dictionary user->passwd
database = {}
registeredUser_L = []

with open(uncrypted, "r") as ofp:
    for line in ofp:
        user,passwd = line.split("@")
        database[user] = passwd.replace("\n", "")
        userList.append(user)

crypt(uncrypted,crypted,key)


registeredUser = "Registered users |"
for user in userList :
     registeredUser += user+"|"

#^^^^^^^^^^^^^^^^^^^am satisfied until there^^^^^^^^^^^^^^^^^^^

while True:
    print(f"\n{registeredUser}")
    currentUser = input("Username \n> ")
    if currentUser in database:
        test_mdp = getpass.getpass(f"Password for {currentUser} \n> ")
        if test_mdp == database[currentUser]:
            break
        else:
            print("Incorrect password, back to username")
    else:
        print("Invalid username")


del database
print(f"Logged in as {currentUser}")

#-------------------------Main code----------------------------
#TODO trying object oriented commands for a better mainloop
#Creating a new user
def createuser():
    print(registeredUser)
    newUser = input("New username > ")
    
    while newUser in userList :
        print("Username already taken")
        newUser = input("new username > ")
    
    newPasswd = getpass.getpass(f"Password for {newUser}\n> ")

    crypt(crypted,uncrypted,key)
    with open(uncrypted,"a") as file :
        file.write(f"\n{newUser}@{newPasswd}")
    crypt(uncrypted,crypted,key)

    print(f"New user {newUser} successfully created ")



#TODO Filesystem, filemanagment


def admin():
    #allows you to see the decrypted file to lookout for problems
    if currentUser == "admin":
        crypt(crypted,uncrypted,key)
        a = input("you admined >")
        a += ""
        crypt(uncrypted,crypted,key)
    else :
        print("You don't have the permissions to run this command")

def logout():
    print("\nyou succesfully logged out as " + currentUser)
    time.sleep(.75)
    sys.exit(0)

tmp = time.strftime("%d %B %Y %H:%M:%S")
print(tmp + " > Version fully fonctinnal")


#fill this as commands get added
commands= ["logout","admin","create user","help"]

def i_need_help_because_i_may_or_may_not_suck_help_me_step_uku_i_am_stuck_that_is_why_i_am_here():
    print("here are the currently active commands :\n|",end="")
    for e in commands :
        print(e,end="|")
    print("")


#mainloop (needs to improve this)
print("\nCommand prompt")

while True:
    command = input("\main>")
    match command:
        case "admin" | "a":
            admin()
        case "penis" | "p":
            print("heheheha panis")
        case "create user":
            createuser()
        case "help":
            i_need_help_because_i_may_or_may_not_suck_help_me_step_uku_i_am_stuck_that_is_why_i_am_here()
        case "logout":
            logout()
