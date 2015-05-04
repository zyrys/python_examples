mode = raw_input('choose mode(encrypt or decrypt)')
message = raw_input('type message: ')
translated = ''
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = input('choose step: ')	

message = message.upper()

print message


for znak in message:
	if znak in letters:
		num = letters.find(znak)
		if mode == 'encrypt':
			num = num + key
		elif mode == 'decrypt':
			num = num - key
		if num >= len(letters):
			num = num - len(letters)
		elif num < 0:
			num = num + len(letters)

		translated = translated + letters[num]

	else:
		translated = translated + znak

print translated


spam = 'ho'
for i in spam:
	spam += i
print spam

for key in range(len(letters)):
	translated1 = ''
	
	for symb in translated:
		if symb in letters:
			num1 = letters.find(symb)
			num1 = num1 - key

			if num1 < 0:
				num1 = num1 + len(letters)
			
			translated1 = translated1 + letters[num1]

		else:
			translated1 = translated1 + symb

	print('Key #%2s: %s' % (key, translated1))
