import detectenglish, cipher_decrypt

def main():
	myMessage = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""

    	hackedMessage = hackTransposition(myMessage)

	if hackedMessage == None:
		print 'failed to hack encryption'
	else:
		print 'Copying hacked message to clipboard: '
		print hackedMessage
		
def hackTransposition(message):
	print 'Hacking...'

	print 'press Ctrl-C or Ctrl-D to quit any time...'

	for key in range(1, len(message)):
		print 'trying key #%s...' %key

		decryptedText = cipher_decrypt.decryptmessage(key, message)

		if detectenglish.isEnglish(decryptedText):
			print()
			print 'possible encryption hack: '
			print 'key %s: %s ' % (key, decryptedText[:100])
			print 'enter d for done or just press enter to continue: '
			response = raw_input('>')
			
			if response.strip().upper().startswith('D'):
				return decryptedText
	return None

if __name__ == '__main__':
	main()