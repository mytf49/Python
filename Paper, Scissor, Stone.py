import random

countwin = 0

pss=['Paper','Scissor','Stone']

def checkwin(userpick,compick):
  if(((userpick == 'Paper') and (compick == 'Stone')) or ((userpick == 'Scissor') and (compick == 'Paper')) or ((userpick == 'Stone') and (compick == 'Scissor'))):
   return True
  else:
   return False

for n in range(1,4):
 compick = random.choice(pss)
 userpick = input("Enter your choice:(Paper, Scissor, Stone): ")
 print("User:", userpick, "Computer:", compick)
 win = checkwin(userpick,compick)
 if win:
   countwin = countwin + 1
   print("You win")
 else:
   print("You don't win")
print("You win", countwin,"out of 3 games")