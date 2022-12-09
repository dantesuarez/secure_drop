import os
import encryption

# This file is for testing purposes only and does not play
# any role in the final project.  This file is used
# to decrypt specified files in order to see things
# such as if data was stored correctly

encryption.decrypt("users.txt", "filekey.key")
encryption.decrypt("passwords.txt", "filekey.key")

while(True):
	option = input("Other files (type 'n' to skip): ")
	if(option == 'n' or option == 'N' or option == ''):
		break
	else:
		encryption.decrypt(option, "filekey.key")
		print(option + "decrypted\n")
		continue

print("done decrypting")