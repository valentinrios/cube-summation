from matrix import Matrix

ok = False

while ok == False:
	try:			
		test_cases = int(raw_input("Test Cases: "))
		if test_cases < 1 or test_cases > 50:
			print "Invalid Number!"
			ok = False
		else:
			ok = True		
	except ValueError as e:
		print 'Invalid Number Format!'

ok = False
for x in xrange(0,test_cases):
	print 'HOLA', x
	while ok == False:
		try:
			matrix_size = int(raw_input("Matrix Size: "))
			if matrix_size < 1 or matrix_size > 100:
				print "Invalid Number!"
				ok = False
			else:
				ok = True
			number_operations = int(raw_input("Number Operations: "))
			if number_operations < 1 or number_operations > 1000:
				print "Invalid Number!"
				ok = False
			else:
				ok = True
		except ValueError as e:
			print 'Invalid Number Format!'
	
	matrix = Matrix(matrix_size)
	print matrix.get_matrix()


	while number_operations != 0:
		input_string = raw_input("Request: ")
		ise = input_string.split(" ")
		if ise[0] == "UPDATE":
			try:			
				if all(x > matrix_size for x in (ise[1],ise[2],ise[3])):
					print "Invalid UPDATE position!"
				else:
					matrix.update_value(ise[1],ise[2],ise[3],ise[4])
					print ">: OK"		
					number_operations = number_operations -1
			except Exception as e:
				print 'Invalid UPDATE Format!'
		elif ise[0] == "QUERY":
			try:
				if ise[1]>ise[4] or ise[2]>ise[5] or ise[3]>ise[6]:
					print "Invalid QUERY position!"
				else:
					print ">:", matrix.query(ise[1],ise[2],ise[3],ise[4],ise[5],ise[6])
					number_operations = number_operations -1
			except Exception as e:
				print 'Invalid QUERY Format!'
		else:
			print 'Invalid Request!'

	ok = False