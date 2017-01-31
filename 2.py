

def count_1s(L):
	counter = 0 
	for i in L:
		if i == 1:
			counter +=1
	return counter


assert(count_1s([1,1,1,1,1,1]) == 6)
assert(count_1s([1,1,1,1,0,1]) == 5)
assert(count_1s([]) == 0)
assert(count_1s([0,0,0,0,0,0,0,0,0]) == 0)


def sum_list(L):
	counter = 0 
	for i in L:
		counter += i 
	return counter

assert(sum_list([1,1,1]) == 3)
assert(sum_list([]) == 0)
assert(sum_list([1,2,3]) == 6)
assert(sum_list(range(10)) == 45)


def sum_upto(n):
	counter = 0
	L = range(n + 1)
	for i in L: 
		counter +=i
	return counter
	

assert(sum_upto(1) == 1)
assert(sum_upto(2) == 3)
assert(sum_upto(3) == 6)
assert(sum_upto(9) == 45)
assert(sum_upto(100) == 5050)


