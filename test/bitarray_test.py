from bitarray import bitarray

a = bitarray()
a.append(True)
a.extend([False, True, True])
bitarray('1011')

############################################################
# Different Instantiations
############################################################

b = bitarray(2**20) 	# bitarry of length 1048576
bitarray('1001011')		# from a string
lst = [True, False, False, True, False, True, True]
bitarray(lst)			# from list, tuple, interable
bitarray('1001011')

print(a)