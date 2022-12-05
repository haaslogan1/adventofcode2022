# The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. 
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

# Same game, but:
# X = lose
# Y = draw
# Z = win

def main():
	# open the input file
	f = open('input.txt','r')
	
	# start total at 0
	total = 0	
	
	# Loop to get total scpre
	for line in f:
		
		opp = 0
		you = 0
		
		# Skip the last line
		if (line == '\n'):
			continue
		
		# get default score
		ds = defaultScore(line[2])
		
		gs = 0
		# get score from opp value
		if (ds == 0):
			gs = lose(line[0])
		elif (ds == 3):
			gs = draw(line[0])
		else:
			gs = win(line[0])
		
		# add game score + default score
		total += (gs + ds)
	
	# print total
	print('total: ' + str(total))
		

# switch case to find default score
def defaultScore(arg1):
	switcher = {
		'X': 0,
		'Y': 3,
		'Z': 6
	}
	
	return switcher.get(arg1, 0)

# switch case to find game score - throwing rock
def win(arg1):
	switcher = {
		'A': 2,
		'B': 3,
		'C': 1
	}
	
	return switcher.get(arg1, 7)
	
# switch case to find game score - throwing paper
def lose(arg1):
	switcher = {
		'A': 3,
		'B': 1,
		'C': 2
	}
	
	return switcher.get(arg1, 7)
	
# switch case to find game score - throwing scissors
def draw(arg1):
	switcher = {
		'A': 1,
		'B': 2,
		'C': 3
	}
	
	return switcher.get(arg1, 7)
	


if __name__ == "__main__":
  main()
