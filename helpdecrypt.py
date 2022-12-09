import os
import encryption

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