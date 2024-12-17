import string
alphabet = string.printable + "éèêàôëùïü"

def cesar_cipher(message, key):

	crypted_message = ""
	for char in message:
		"""
		on va chiffrer le caractère 
			1- trouver la positon du carac dans l'alphabet
			2- y rajouter la clef à la positon du carac dans l'alphabet
			3- reccupérer le caractère chiffré
		on va stocker le caractère chiffrer
		"""
		index_carac_in_printable = alphabet.index(char)
		index_crypted_char = (index_carac_in_printable + key) % len(alphabet)
		cryted_char = alphabet[index_crypted_char]

		crypted_message += cryted_char
	
	return crypted_message


def cesar_uncipher(crypted_message, key):
	return cesar_cipher(crypted_message, -key)



def brute_force_cesar_cipher(crypted_message):
	for possible_key in range(0, len(alphabet)):
		print(cesar_uncipher(crypted_message, possible_key))
		print("_"*15)

if __name__ == "__main__":
	# crypted_message = cesar_cipher("salut les bgs aujourd'hui on va corriger l'exercice", 13)
	# print(crypted_message)
	# brute_force_cesar_cipher(crypted_message)

	crypted_message = cesar_cipher("salut les bgs aujourd'hui on va corriger l'exercice", 3)
	print(crypted_message)
	original_message = cesar_uncipher(crypted_message, 3)
	print(original_message)


	print("coucou")
	print("hello")