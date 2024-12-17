from cesar import cesar_uncipher, cesar_cipher



def vigenere_cipher(message, password, reverse=False):
	list_of_keys = [alphabet.index(char) for char in password] # convert password to a list of keys
	crypted_message = ""
	
	for index, char in  enumerate(message):
		current_key = list_of_keys[index % len(list_of_keys)]
		crypted_message += cesar_uncipher(char, current_key) if reverse else cesar_cipher(char, current_key)

	return crypted_message

