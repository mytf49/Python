def lcm(x, y):
    if x < 0 or y < 0:
       print("Please enter a positive number")
    if x > y:  
       greater = x  
    else:  
       greater = y  
    while(True):  
      if((greater % x == 0) and (greater % y == 0)):  
       lcm = greater  
      break  
    greater += 1  
    return lcm 
 
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))  