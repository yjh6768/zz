def TimesTable(arg):
	table = []
	for j in xrange(1,11):
		table.append(str(arg)+"*"+str(j)+"="+str(arg*j))
	return table

# for i in range(0,10):
	#print TimesTable(2)[i]
re = TimesTable(2)	

print re
for r in re:
	print re
input = 2

timetable=[]
for i in xrange(2,6):
	for j in xrange(1,11):
		timetable.append(str(i) + " * "+ str(j) + " = "+str(i*j) + "    " +str(i+4)+"*"+str(j)+"="+str((i+4)*j))
for i in timetable:
	print i