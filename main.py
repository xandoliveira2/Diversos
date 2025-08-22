import math


def first_n_primes(numberofprimes):
	if numberofprimes < 6:
		limit = 15
	else:
		limit = int(numberofprimes * (math.log(numberofprimes) + math.log(math.log(numberofprimes)))) + 10
	# print(bin((1 << (limit+1 ))-1))
	# print(bin((3 << (limit-1))))
	
	# casasdecimais = (3 << (limit-1)).bit_length()
	# print(casasdecimais)
	# sieve = ((1 << (limit+1 ))-1) ^ (3 << (limit-1))

	"""
    1111111111100
	"""
	limit = limit -1

	# print(bin(p1))
	sieve = ((1 << limit)-1) << 2
	print(bin(sieve))

	for i in range(2,int(math.sqrt(limit)) + 1):
		if (sieve >> i) & 1 == 1:
			for j in range(i * i, limit + 1, i):
				sieve = sieve & ~(1 << j)

	print(bin(sieve))
	primes = [i for i in range(1,sieve.bit_length()+1) if (sieve >> i) & 1 == 1]


	return primes[:numberofprimes]

# def first_n_primes(numberofprimes):
# 	if numberofprimes < 6:
# 		limit = 15
# 	else:
# 		limit = int(numberofprimes * (math.log(numberofprimes) + math.log(math.log(numberofprimes)))) + 10

# 	sieve = [True] * (limit + 1)
# 	sieve[0] = sieve[1] = False
# 	for i in range(2,int(math.sqrt(limit)) + 1):
# 		if sieve[i]:
# 			for j in range(i * i, limit + 1, i):
# 				sieve[j] = False

# 	primes = [i for i,is_p in enumerate(sieve) if is_p]

# 	return primes[:numberofprimes]


print(first_n_primes(4))