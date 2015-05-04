def main():
	myMessage = raw_input('type your message: ')
	mykey = 3
	
	ciphertext = encryptmessage(mykey, myMessage)

	print(ciphertext + '|')

def encryptmessage(key, message):
	
	ciphertext = [''] * key
	
	for col in range(key):
		pointer = col
		

		while pointer < len(message):
			ciphertext[col] += message[pointer]
			pointer += key 

	return ''.join(ciphertext)

if __name__ == '__main__':
	main()