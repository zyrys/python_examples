def liczba(x):
	return([n for n in range(0, x) if x%4 != 0 and x%9 != 0])

l = liczba(5)
print l
