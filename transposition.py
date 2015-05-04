import random, sys, cpiher_encrypt, cipher_decrypt

def main():
	random.seed(42)
	
	for i in range(20):
		message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

		message = list(message)
		random.shuffle(message)
		message = ''.join(message)

		print('test #%s: "%s..."' %(i+1, message[:50]))

		for key in range(1, len(message)):
			encrypted = cpiher_encrypt.encryptmessage(key, message)
			decrypted = cipher_decrypt.decryptmessage(key, encrypted)

			if message != decrypted:
				print 'missmatch with key %s and message %s...' %(key, message[:20])
				print decrypted[:20] + '...'
				sys.exit()

if __name__ == '__main__':
	main()