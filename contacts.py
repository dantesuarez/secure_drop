import time
import os
import encryption

#function to add contact to a user
def add_contact(user, name, email):

	#split user name at the @ symbol for file name
	split_user = user.split('@')
	user = split_user[0]

	#create / open a contact file for the current user
	contact_file = open(user + "_contacts.txt", "a")

	# Makes sure the file is not empty before decrypting
	# This is because if the file is empty it means it was
	# just created with the line above and is therefore not
	# encrypted
	if(os.path.getsize(user + "_contacts.txt") != 0):
		encryption.decrypt(user + "_contacts.txt", "filekey.key")

	#Check to make sure user exists
	with open("users.txt", 'r') as user_file:
		encryption.decrypt("users.txt", "filekey.key")
		# read all content of a file
		content = user_file.read()
		if email not in content:
			print("No account registered with specified email\n")
			print("Try again...\n")
			user_file.close()
			encryption.encrypt("users.txt", "filekey.key")
			return
		else:
			user_file.close()
			encryption.encrypt("users.txt", "filekey.key")

	#writes contact name to file
	contact_file.write(name)
	contact_file.write('\n')

    #writes email to contact file
	contact_file.write(email)
	contact_file.write('\n')

    #close file object 
	contact_file.close()
	encryption.encrypt(user + "_contacts.txt", "filekey.key")

	time.sleep(1)
	print("Contact has been created")

def list_contacts(user):
	print("Contacts of: " + user + "\n")

	# Splits user name at the @ symbol for file name purposes
	split_user = user.split('@')
	user = split_user[0]

	# Checks to see if the user has a contact file,
	# if not, cannot list contacts
	if (os.path.exists(user + "_contacts.txt")) == False:
		print("Contact file for this user does not exist")
		return

	# decrypt contact file
	encryption.decrypt(user + "_contacts.txt", "filekey.key")
	contact_file = open(user + "_contacts.txt", "r")

	# If the file is empty the user has no contacts
	# else read the file and print the contacts
	if os.path.getsize(user + "_contacts.txt") == 0:
		print("User has no contacts. Please create a contact")
		contact_file.close()
		encryption.encrypt(user + "_contacts.txt", "filekey.key")
		return
	else:
		file_content = contact_file.read()
		print(file_content)
		contact_file.close()
		encryption.encrypt(user + "_contacts.txt", "filekey.key")
		return

