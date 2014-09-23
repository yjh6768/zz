def TimesTable(arg):
	table=[]
	for j in xrange(1,11):
		table.append(str(arg) + " * "+ str(j) + " = "+str(arg*j))
	return table

for i in range(0,10):
	print TimesTable(2)[i]