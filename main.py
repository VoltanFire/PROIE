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
        passwd = passwd.replace("\n", "")
        database[user] = passwd
        registeredUser_L.append(user)

crypt(uncrypted,crypted,key)


registeredUser = "Registered users |"
for user in registeredUser_L :
     registeredUser += user+"|"


"""
#old registering
currentUser = input("Username : ")
while currentUser not in database:
    print("Invalid username")
    currentUser = input("Username : ")

#Password checking
while True:
    test_mdp = getpass.getpass("Password for " + currentUser + " user : ")
    if test_mdp != database[currentUser]:
        print("Password doesn't match user :" + currentUser)
        time.sleep(.5)
        pass
    else :
        break
"""


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

#--------------------------CODE----------------------------

#Creatinga a new user
def createuser():
    print(registeredUser)
    newUser = input("New username > ")
    
    while newUser in registeredUser_L :
        print("Username already taken")
        newUser = input("new username > ")
    
    newPasswd = getpass.getpass(f"Password for {newUser}\n> ")

    crypt(crypted,uncrypted,key)
    with open(uncrypted,"a") as file :
        file.write(f"\n{newUser}@{newPasswd}")
    crypt(uncrypted,crypted,key)

    print(f"New user {newUser} successfully created ")






#TODO Filemanagment



def admin():
    if currentUser == "admin":
        crypt(crypted,uncrypted,key)
        a = input("you admined >")
        a += ""
        crypt(uncrypted,crypted,key)
    else :
        print("you know Y")

def logout():
    print("you succesfully logged out as " + currentUser)
    sys.exit()

tmp = time.strftime("%d %B %Y %H:%M:%S")
print(tmp + " > Version fully fonctinnal")



#mainloop

commands= ["logout","admin","create user","help"]
def i_need_help_because_i_may_or_may_not_suck_help_me_step_uku_i_am_stuck_that_is_why_i_am_here():
    print("here are the currently active commands :\n|",end="")
    for e in commands :
        print(e,end="|")
    print("")

print("\nCommand prompt")
while True:
    command = input(">")
    if command not in commands:
        print("Unkown command")
    elif command == "admin":
        admin()
    elif command == "help":
        i_need_help_because_i_may_or_may_not_suck_help_me_step_uku_i_am_stuck_that_is_why_i_am_here()
    elif command == "create user":
        createuser()
    elif command == "logout":
        logout()
    else :
        time.sleep(.25)
        pass

