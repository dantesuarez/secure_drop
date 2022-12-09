import os
import encryption

# This file is for testing purposes only and does not play
# any role in the final project.  This file is used
# to encrypt specified files after testing. This
# file needs to exist because our main driver expects to 
# see encrypted files. So after testing it is required to 
# re-encrypt them

encryption.encrypt("users.txt", "filekey.key")
encryption.encrypt("passwords.txt", "filekey.key")

while(True):
	option = input("Other files (type 'n' to skip): ")
	if(option == 'n' or option == 'N' or option == ''):
		break
	else:
		encryption.encrypt(option, "filekey.key")
		print(option + "encrypted\n")
		continue

print("done encrypting")