fileobj = open('somefile','w')
for i in range(3):
	record = ''            # start with a null string
	for j in range(1,4):
		record += str(i*3+j) + ','  # append each value and comma
	record = record[:-1]            # strip off the last comma 
	fileobj.write(record)
	if i < 2:
	fileobj.write('\n')         # no \n on last record!  
fileobj.close() 
