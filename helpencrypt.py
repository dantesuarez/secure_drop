import os
import encryption

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