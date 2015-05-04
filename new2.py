class produkt:

	__ilosc = 0
	def __init__(self):
		self.__ilosc = 111
	def ustaw_ilosc(self, ilosc):
		self.__ilosc = ilosc

class pomidor(produkt):
	def __init__(self):
		produkt.__init__(self)
		self.ilosc = 10
	opis = 'swieze pomidory z syberii'
	
p = pomidor()
print p._produkt__ilosc
print p.ilosc
print p.opis