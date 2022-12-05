def main():
	# open the input file
	f = open('input.txt','r')
	
	# initialize total -> 0
	total = 0
	
	# get all lines
	lines = f.readlines()
	
	# loop through each line of the file
	i = 0
	while i < len(lines):
		
		# get next three lines
		line1, line2, line3 = lines[i], lines[i+1], lines[i+2]
		
		# iterate i
		i += 3
		
		# find match char
		set_string1, set_string2, set_string3 = set(line1), set(line2), set(line3)
		matched_char = set_string1 & set_string2 & set_string3
		matc = str(next(iter(matched_char)))
		
		# remove and get the next character if the character is a new line.
		if (matc == '\n'):
			matched_char.pop()
			matc = str(next(iter(matched_char)))
		
		# get value of char, and add it to total
		if (str(matc).isupper()):
			total += (ord(matc) - 38)
		else:
			total += (ord(matc) - 96)
		
	
	print('total ' + str(total))
		

if __name__ == "__main__":
  main()