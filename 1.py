

#A prime number (or a prime) is a natural number greater than 1 
#that has no positive divisors other than 1 and itself.

def is_prime(n):
	if (n <= 1):
		return False
	for i in range(2, n):
		#2, 3, 4, 5 ..., n - 1
		if (n % i == 0):
			return False
	return True


assert(is_prime(1) == False)
assert(is_prime(2) == True)
assert(is_prime(3) == True)
assert(is_prime(4) == False)
assert(is_prime(5) == True)
assert(is_prime(6) == False)

#Write the function pi(n) (which has nothing much to do with the 
#3value "pi", but coincidentally shares its name) that takes an integer 
#n and returns the number of prime numbers less than or equal to n.
def count(L):
	n = 0 
	for i in L:
		n += 1
	return n 
assert(count([1,2,3,4]) == 4)
assert(count([]) == 0)
assert(count([1,1,1,11,1,1,1]) == 7)

def pi(n):
	counter = 0 
	for element in range(n + 1):
		if (is_prime(element)):
			counter +=1
	return counter


assert(pi(1) == 0)
assert(pi(2) == 1)
assert(pi(3) == 2)
assert(pi(4) == 2)
assert(pi(5) == 3)
assert(pi(100) == 25) 




