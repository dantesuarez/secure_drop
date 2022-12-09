from cryptography.fernet import Fernet

# Encrypt function for security purposes
def encrypt(file2encrypt, key4encryption):
	# opening the key
	with open(key4encryption, 'rb') as filekey:
		key = filekey.read()

	# using the generated key
	fernet = Fernet(key)

	# opening the original file to encrypt
	with open(file2encrypt, 'rb') as file:
		original = file.read()
    
	# encrypting the file
	encrypted = fernet.encrypt(original)

	# opening the file in write mode and
	# writing the encrypted data
	with open(file2encrypt, 'wb') as encrypted_file:
		encrypted_file.write(encrypted)

#decrypt json file so it can be accessed by code
def decrypt(file2decrypt, key4decryption):
   # opening the key
	with open(key4decryption, 'rb') as filekey:
		key = filekey.read()

	# using the key
	fernet = Fernet(key)
    
	# opening the encrypted file
	with open(file2decrypt, 'rb') as enc_file:
		encrypted = enc_file.read()
    
	# decrypting the file
	decrypted = fernet.decrypt(encrypted)
    
	# opening the file in write mode and
	# writing the decrypted data
	with open(file2decrypt, 'wb') as dec_file:
		dec_file.write(decrypted)