def main():
  # open the input file
  f = open('input.txt','r')
  
  # set the maximum value
  maxi = 0
  
  #set the min value
  total = 0
   
  # count elves
  counta = 0
  
  # top 3 elves
  elves = [0, 0, 0]
   
  # traverse every line in the file
  for line in f:
    
    # skip the line IF it is a new line, restart with the next  
    # otherwise, continue adding to the total
    if line != '\n':
      total += int(line)
    else:
      # add one elf
      counta += 1
      # reset counter
      total = 0
        
    # set maximum value to total IF total is greater
    if total > maxi:
      maxi = total
      
    # check for top 3 elves
    if total > elves[0]:
      elves[0] = total
      # re-sort elves
      elves = sorted(elves)
     
  # close the reader
  f.close()
     
  print('top 3 elves:' + str(elves))
  print(sum(elves))
  print('elf count: ' + str(counta))
  print('maximum value: ' + str(maxi))     
     

if __name__ == "__main__":
  main()
