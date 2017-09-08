numands = 0

f = open('hp.txt', 'rw')
line = f.readline()

while(line != ""):

	words = line.split(" ")
	for word in words:
		if word == "and":
			numands = numands + 1
	line = f.readline()

print numands