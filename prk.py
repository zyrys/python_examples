import math

print 'program oblicza pierwiastki kwadratowe rownania o postaci ax^2+bx+c'
a = raw_input('Podaj parametry a: ')
b = raw_input('Podaj parametry b: ')
c = raw_input('Podaj parametry c: ')

try:
	a, b, c = float(a), float(b), float(c)
	if a < 0 or a > 10:
		raise RuntimeError, 'Za duza liczba'
except ValueError:
	print 'To mialy byc liczyby'
	exit()
except RuntimeError, error:
	print 'Uwaga ', error
	exit()

if a == 0:
	print 'wspolczynnik a rozny od zera( to nie funkcja liniowa)'
	exit()

delta = b*b-4*a*c

if delta < 0:
	print 'brak pierwiastkow rzeczywistych'

elif delta == 0:
	pierwiastek = -b/2*a
	print 'delta < 0, pierwaistek to: ', pierwiastek
else:
	pierwiastek1 = (-b+math.sqrt(delta))/2*a 
	pierwiastek2 = (-b-math.sqrt(delta))/2*a 
	print 'pierwiastki to: ', pierwiastek1, pierwiastek2
