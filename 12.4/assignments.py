import re

def main():
	# open the input file
	f = open('input.txt','r')
	
	# initialize total -> 0
	total = 0
	
	# loop through each line of the file
	for line in f:
		# Create a map object containing all 4 ints in the line
		vals = map(int, re.findall(r'\d+', line))
		
		# assign each int of the line
		i1 = next(vals)
		i2 = next(vals)
		i3 = next(vals)
		i4 = next(vals)
		
		# check whether or not one subset fully contains the other
		if (i1 <= i3 and i2 >= i4):
			total += 1
		elif (i3 <= i1 and i4 >= i2):
			total += 1
	
	# print the total amount of fully overlapping assignments
	print("There are " + str(total) + " fully overlapping assignments!")
			
		
if __name__ == "__main__":
  main()
