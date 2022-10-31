import time
import os

#
# Dante Suarez
# 10/15/2022
#

#Function to ensure username is correct format
def auth_user(username):

    #at symbol and suffixes that an email needs
    at_sym = '@'
    endings = ['.com', '.net', '.org', '.edu', '.gov']

    #if @ symbol is not in the username it is invalid
    if not at_sym in username:
        return False

    #loop goes through the endings, checking if the username has one of them
    index = 0
    while index <= 4:
        if endings[index] in username:
            break
        index = index + 1
    
    #if index gets to 5 that means the username did not contain any of the suffixes
    #therefore it is not a valid email
    if index == 5:
        return False

    return True

#Function makes sure no accounts are made with repeating emails
def repeat_user(username):
    user_file = open("users.txt", "r")

    #gets first user
    poss_user = user_file.readline()
    clean_user = poss_user[:-1]    

    #if the file size is 0, then no users have been created, therefore there cannot be repeats
    if os.path.getsize("users.txt") == 0:
        return True

    #if the username matches the first one in the username file, then it is a repeat
    if username == clean_user:
        user_file.close()
        return False

    #check the rest of the usernames for repeats
    while username != clean_user:
        poss_user = user_file.readline()
        clean_user = poss_user[:-1]

        #if there is a repeat return false
        if username == clean_user:
            user_file.close()
            return False

        #if we get to the end of the file, break and return true, username wasn't a repeat
        if clean_user == '':
            break


    user_file.close() 
    return True

# Compares password associated with the username to the given password
def loginauth(username, password):

    #open file objects
    user_file = open("users.txt", "r")
    pass_file = open("passwords.txt", "r")

    #read first line of username file
    potential_user = user_file.readline()

    #remove newline character so username is clean
    clean_user = potential_user[:-1]

    #iterator
    x = 0

    #loop through usernames until username matches
    while(username != clean_user):
        potential_user = user_file.readline()
        clean_user = potential_user[:-1]
        x = x + 1

    #read password file into all_passes variable
    all_passes = pass_file.readlines()

    #match password to the line that the username was found on
    potential_pass = all_passes[x]
    clean_pass = potential_pass[:-1]

    #if the password matches, success
    if(password == clean_pass):
        print("Success")
        user_file.close()
        pass_file.close()
        return True

    #if username or password was not found, or the password doesn't match
    #return False
    user_file.close()
    pass_file.close()

    return False

# Login
def login():
    #gets username, makes sure it isn't blank
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
        else:
            break
    
    #gets password, makes sure it isn't blank
    while True:
        password = input("Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break

    #authenticate login credentials
    if loginauth(username, password):
        return session(username)
    else:
        print("Invalid username or password")

# Register
def register():
    #open files for appending
    user_file = open("users.txt", "a")
    pass_file = open("passwords.txt", "a")

    #takes email
    while True:
        username = input("Email address: ")
        if not len(username) > 0:
            print("Email can't be blank")
            continue
        elif not auth_user(username):
            print("Not a valid email address\n")
            print("Email address must contain '@' and one of the following suffixes:\n")
            print(".com, .net, .org, .edu, .gov\n")
            continue
        elif not repeat_user(username):
            print("There is already an account under this address.\n")
            continue
        else:
            break
            

    #takes new password
    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        else:
            break
    print("Creating account...")

    #writes username to file
    user_file.write(username)
    user_file.write('\n')

    #writes password to password file
    pass_file.write(password)
    pass_file.write('\n')

    #close file objects 
    user_file.close()
    pass_file.close()

    time.sleep(1)
    print("Account has been created")

# User session
def session(username):
    print("Welcome to your account " + username + "\n")
    menu = "Options: help | logout\n"
    print(menu)

    while True:
        option = input(username + " > ")
        if option == "help":
            print(menu)
        elif option == "logout":
            print("Logging out, goodbye...")
            break
        else:
            print(option + " is not an option")
            
        


# ON START
print("Welcome to the system. Please register or login.")
print("Options: register | login | exit")

while True:
    option = input("> ")
    if option == "login":
        login()
    elif option == "register":
        register()
    elif option == "exit":
        break
    else:
        print(option + " is not an option")


# ON EXIT
print("Shutting down...")
time.sleep(1)
