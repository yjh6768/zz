def TimesTable(arg):
	table=[]
	for j in xrange(1,11):
		table.append(str(arg) + " * "+ str(j) + " = "+str(arg*j))
	return table

re = TimesTable(2)
ge = TimesTable(3)
he = TimesTable(4)
ke = TimesTable(5)
print re
for r in re:
	print r
print ge
for g in ge:
	print g
print he
for h in he:
	print h
print ke
for k in ke:
	print k

for r in re:
	print r+'   '+g+'   '+h+'   '+k