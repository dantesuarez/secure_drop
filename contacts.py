import time
import os

#function to add contact to a user
def add_contact(user, name, email):

	#split user name at the @ symbol for file name
	split_user = user.split('@')
	user = split_user[0]

	#create / open a contact file for the current user
	contact_file = open(user + "_contacts.txt", "a")

	#writes contact name to file
	contact_file.write(name)
	contact_file.write('\n')

    #writes email to contact file
	contact_file.write(email)
	contact_file.write('\n')

    #close file object 
	contact_file.close()

	time.sleep(1)
	print("Contact has been created")

def list_contacts(user):
	print("Contacts of: " + user + "\n")

	split_user = user.split('@')
	user = split_user[0]

	if (os.path.exists(user + "_contacts.txt")) == False:
		print("Contact file for this user does not exist")
		return

	contact_file = open(user + "_contacts.txt", "r")

	if os.path.getsize(user + "_contacts.txt") == 0:
		print("User has no contacts. Please create a contact")
		contact_file.close()
		return
	else:
		file_content = contact_file.read()
		print(file_content)
		contact_file.close()
		return

