from bitarray import bitarray

# https://pypi.python.org/pypi/bitarray/
# bitarray(bitarray, endian="little|big")


a = bitarray()
a.append(True)
a.extend([False, False, True])
b = bitarray('1011')
print('######################################')
print(a)	# 
print(b)	# a & b should be equivalent

############################################################
# Different Instantiations
############################################################

print('######################################')
c = bitarray(2**6) 		# bitarry of length 64 || initialized with GARBAGE values
bitarray('1001011')		# from a string
lst = [True, False, False, True, False, True, True]
d = bitarray(lst)		# from list, tuple, interable
e = bitarray('1001011')	# initialize with string

# Can be assigned from any Python object, if value can be interpreted as a truth value
#	Think of a bool() casting applied to all objects

f = bitarray([42, '', True, {}, 'foo', None])
g = bitarray('101010')
rand = bitarray('11')

print(c)
print(d)	#
print(e)	# d & e should be equivalent
print(f)	#
print(g)	# f & g should be equivalent

rand.append(rand)
print(rand) 			# 111 since bool(rand) == true
print(rand.count(bool(rand)))	# counts number of True
print(rand.count(0))	# counts number of False

############################################################
# Supports Slice and Deletion List Operations
############################################################

print('######################################')
k = bitarray(50)
print(k)
k.setall(False)
print(k)
k[11:37:3] = 9 * bitarray([True])	# turns every 3rd element to True from 11-37
print(bool(9 * bitarray([True])))
print(k)
del k[12::3]	# delete every 3rd element starting w/ 12
print(k)

############################################################
# Endians [Ordering L-R || R-L for bit significance]
############################################################

print('######################################')

m = bitarray(endian='little')	#little is MostSig <-------> LeastSig
m.frombytes(b'A')				# how to convert strings to binary
print(m)

n = bitarray(endian='big')		#big is LeastSig <-------> MostSig
n.frombytes(b'A')
print(n)

# important bitwise operations (&, |, ^, &=, |=, ^=, ~)
# however be carefuly when apply to bitarrys with different endians
# Other functions: tobytes, frombytes, tofile and fromfile

