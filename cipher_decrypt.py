import math

def main():

	myMessage = 'Cenoonommstmme oo snnio. s s c' 
	mykey = 8

	plaintext1 = decryptmessage(mykey, myMessage)
	print plaintext1 + '|'


def decryptmessage(key, message):

	### tutaj trzeba cos zmienic zeby zaokraglal w gore 
	### +1 nie bedzie dzialac gdy wynik dzielenia bedzie bez reszty!!!!
	### len(message) zwracalo in a nie float i to dawalo wynik dla liczb calkowitych
	numofcol = math.ceil(float(len(message))/key)
	
	
	
	numofrow = key
	numofshaded = (numofcol * numofrow) - len(message)
	
	plaintext = [''] * int(numofcol)

	col = 0
	row = 0
	
	for symbol in message:
		plaintext[col] += symbol
		col += 1

		if (col == numofcol) or (col == numofcol - 1 and row >= numofrow - numofshaded):
			col = 0
			row += 1

	return ''.join(plaintext)

if __name__ == '__main__':
	main()