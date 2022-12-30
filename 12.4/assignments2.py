import re

def main():
	# open the input file
	f = open('input.txt','r')
	
	# initialize total -> 0
	total = 0
	
	# loop through each line of the file
	for line in f:
		
		# Extract all the ints from the line
		vals = map(int, re.findall(r'\d+', line))
		
		# Assign each int within the map
		i1 = next(vals)
		i2 = next(vals)
		i3 = next(vals)
		i4 = next(vals)
		
		# Check every condition where there could be an overlapping assignment
		if (i1 <= i3 and i2 >= i4):
			total += 1
		elif (i3 <= i1 and i4 >= i2):
			total += 1
		elif (i1 < i3 and i2 < i4 and i2 >= i3):
			total += 1
		elif (i1 > i3 and i2 > i4 and i4 >= i1):
			total += 1
	
	# Print the total amount of overlapping assignments
	print("There are " + str(total) + " overlapping assignments!")
			
		
if __name__ == "__main__":
  main()