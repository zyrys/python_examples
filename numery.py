import string
cyfry = ('zero', 'jeden', 'dwa', 'trzy', 'cztery', 'piec', 'szesc', 'siedem', 'osiem', 'dziewiec')

while True:
	try:
		ciag = raw_input('Wprowadz liczbe: ')
		if ciag == float(ciag):
			raise ValueError, 'to mialy byc liczby(raise)!'
		pass
	except ValueError, error:
		print 'uwaga!', error
		exit()
	else:
		print 'to mialy byc liczby(else ?)'
		break


for cyfra_indeks in [int(x) for x in ciag if x in string.digits]:
	print cyfry[cyfra_indeks],
	