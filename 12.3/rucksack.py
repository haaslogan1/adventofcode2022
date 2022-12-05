def main():
	# open the input file
	f = open('input.txt','r')
	
	# initialize total -> 0
	total = 0
	
	# loop through each line of the file
	for line in f:
		# split line into two
		firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
		
		# find match char
		set_string1, set_string2 = set(firstpart), set(secondpart)
		matched_char = set_string1 & set_string2
		matc = str(next(iter(matched_char)))
		
		print(ord(matc))
		# get value of char, and add it to total
		if (str(matc).isupper()):
			total += (ord(matc) - 38)
		else:
			total += (ord(matc) - 96)
	
	print('total ' + str(total))
		

if __name__ == "__main__":
  main()
