import time
import os
import contacts
import getpass
import encryption

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

    encryption.decrypt("users.txt", "filekey.key")
    encryption.decrypt("passwords.txt", "filekey.key")

    #open file objects
    user_file = open("users.txt", "r")
    pass_file = open("passwords.txt", "r")

    if(os.stat("users.txt").st_size == 0):
        print("No users have been registered. Please register a user.\n")
        print("Exiting...\n")
        return False

    #read first line of username file
    potential_user = user_file.readline()

    #remove newline character so username is clean
    clean_user = potential_user[:-1]

    #iterator
    x = 0

    #loop through usernames until username matches
    while(username != clean_user):
        #print("here\n")
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
        encryption.encrypt("users.txt", "filekey.key")
        encryption.encrypt("passwords.txt", "filekey.key")
        return True

    #if username or password was not found, or the password doesn't match
    #return False
    user_file.close()
    pass_file.close()

    encryption.encrypt("users.txt", "filekey.key")
    encryption.encrypt("passwords.txt", "filekey.key")

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
        password = getpass.getpass(prompt="Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break

    #authenticate login credentials
    if loginauth(username, password):
        return session(username)
    else:
        print("Invalid username or password")

# Simple funtion that takes a string and will return
# true if the string contains a number anywhere
def contains_number(string):
    return any(char.isdigit() for char in string)

# Simple function that returns true if it contains
# any one of the special characters in the special_characters
# string
def contains_special(string):
    special_characters = "!@#$%^&*()-+?_=,<>/"

    return any(char in special_characters for char in string)

# Simple function to check if a string contains a capital letter
def contains_capital(string):
    return any(char.isupper() for char in string)

# Function that verifies our password requirements
# Checks that the password is longer than 11 chars
# Checks that it also contains a number, a capital
# letter, and also a special character
def password_requirements(password):
    if(len(password) <= 11):
        return False
    elif(contains_capital(password)) == False:
        print("No capital in password\n")
        return False
    elif(contains_number(password)) == False:
        print("No number in password\n")
        return False
    elif(contains_special(password)) == False:
        print("No special character in password\n")
        return False
    else:
        return True

# Register user
def register():

    encryption.decrypt("users.txt", "filekey.key")
    encryption.decrypt("passwords.txt", "filekey.key")

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
        password = getpass.getpass(prompt="New Password: ")

        # Make sure password was not left blank
        if not len(password) > 0:
            print("Password can't be blank")
            continue

        # Checks password requirements
        if (password_requirements(password)) == False:
            print("Password must contain the following requirements: \n\n")
            print("> Must be longer than 11 characters\n")
            print("> Must contain a capital letter\n")
            print("> Must contain at least one number\n")
            print("> Must contain a special character\n\n")
            print("Available special characters: @#$%^&*()-+?_=,<>/\n\n")
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

    encryption.encrypt("users.txt", "filekey.key")
    encryption.encrypt("passwords.txt", "filekey.key")

    time.sleep(1)
    print("Account has been created")

# User session
def session(username):
    print("Welcome to your account " + username + "\n")
    menu = "Options: add contact | list contacts | help | logout\n"
    print(menu)

    # Main menu with options:
    # > help -- lists commands
    # > add contact -- adds contact to user
    # > list contacts -- lists users contacts
    # > logout -- logs out of user and drops back to start menu
    while True:
        option = input(username + " > ")
        if option == "help":
            print(menu)
        elif option == "add contact":
            contact_name = input("Full name: ")
            contact_email = input("Email: ")
            contacts.add_contact(username, contact_name, contact_email)
        elif option == "list contacts":
            contacts.list_contacts(username)
        elif option == "logout":
            print("Logging out, goodbye...")
            break
        else:
            print(option + " is not an option")
            
        


# ON START
print("Welcome to the system. Please register or login.")
print("Options: register | login | help | exit")

while True:
    option = input("> ")
    if option == "login":
        login()
    elif option == "register":
        register()
    elif option == "help":
        print("Options: register | login | help | exit\n")
        continue
    elif option == "exit":
        break
    else:
        print(option + " is not an option")


# ON EXIT
print("Shutting down...")
time.sleep(1)
