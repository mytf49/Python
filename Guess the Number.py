a = int(input("Enter the lowest number:"))
b = int(input("Enter the highest number:"))
import random
c = a + random.randrange(b-a+1)
#print(c)
print("Guess a number from "+ str(a) +" to "+str(b) +":")
d = int(input())
if d > c:
  print("The guess is bigger than the answer. The correct number is", c)
elif d < c:
  print("The guess is smaller than the answer. The correct number is", c)
elif d == c:
  print("Corect. You guess the number")