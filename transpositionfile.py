import time, os, sys, cpiher_encrypt, cipher_decrypt, detectenglish

def main():
	inputFilename = 'frankenstein.txt'

	outputFilename = 'frankenstein.encrypt.txt'

	myKey = 10
	myMode = 'encrypt'
	### gdy nie ma takiego pliku programkonczy dzialanie
	if not os.path.exists(inputFilename):
		print 'file %s does not exist. quit...' % inputFilename
		sys.exit()

	if os.path.exists(outputFilename):
		print 'this will overwrite file. (C)ontinue or (Q)uit'
		response = raw_input('>')
		if not response.lower().startswith('c'):
			sys.exit()

	fileObj = open(inputFilename)
	content = fileObj.read()
	fileObj.close()

	print('%sing...' %(myMode.title()))

	startTime = time.time()	
	if myMode == 'decrypt':
		translated = cpiher_encrypt.encryptmessage(myKey, content)
	elif myMode == 'decrypt':
		translated = cipher_decrypt.decryptmessage(myKey, content)
	totalTime = round(time.time() - startTime, 2)
	print ('%sion time: %s seconds' %(myMode.title(), totalTime))

	outputFileObj = open(outputFilename, 'w')
	outputFileObj.write(translated)
	outputFileObj.close()

	print('Done %sing %s (%s characters).' %(myMode, inputFilename, len(content)))
	print('%sed file is %s.' % (myMode.title(), outputFilename))

	new_content = detectenglish.isEnglish(content)
	print new_content
if __name__ == '__main__':
	main()