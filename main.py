#Written by Tanner McCarthy
#sept 27 2021
#prof fried
#Module 5 Homework

#imports the math class to use funcations already made in the math class
from math import sqrt 

#part 1

print("Part 1")

#this is my counter variable
chances  = int(0)

#while loop to keep asking the user until we get an input we like. so it will never end
#on its own 
while True:
  try:
    name = str(input("Please tell me your name: "))
  #this is still here for syntax but i do
  #not expect this to catch any errors bc
  #a string variable will take any letters
  #numbers, and special characters in the #ASCII charts
  except ValueError:
    print("\nINVALID, Please try again\n")
    
    #this incriments chances by one
    #this is the same as writting 
    #chances = chances + 1
    chances +=1
    
    #continue just keeps the program running
    #and jumps out of the indent and stays
    #within the while loop
    continue

  if(name.isalpha() == True):
    break
  else:
    print("\nUnacceptable, please only use the english alphabet.\n")
    
    #this incriments chances by one
    #this is the same as writting 
    #chances = chances + 1
    chances +=1

    #continue just keeps the program running
    #and jumps out of the indent and stays
    #within the while loop
    continue


while True:
  try:
    age = int(input("Please enter your age: "))
  except ValueError:
    print("\nINVALID, Please try again\n")
    
    #this incriments chances by one
    #this is the same as writting 
    #chances = chances + 1
    chances +=1

    #continue just keeps the program running
    #and jumps out of the indent and stays
    #within the while loop
    continue

  #this if checks if the age is greater than
  #or equal to 1 and is less than or equal to
  # 100.
  if age >= 1 and age <= 100:

    #this break us out of the never ending
    #while loop
    break
  
  #else is used if age is less than 1 or
  #greater than 100 
  else:
    print("\nUnacceptable, please only use the english alphabet.\n")
    
    #this incriments chances by one
    #this is the same as writting 
    #chances = chances + 1
    chances +=1

    #continue just keeps the program running
    #and jumps out of the indent and stays
    #within the while loop
    continue


#print(chances)

if chances >= 3:
  print("Unacceptable\n")
else:
  print("Acceptable\n")
#end of part 1

#start of part 2
#extra credit

#printing out a new line to make the console look more clean
print("\nPart 2, Extra Credit")

digit = False
upper = False
lower = False
special = False


while True:
  try:
    print("\ncreate a password that is \n8 or more characters\ncontains a number\nhas an uppercase letter\nhas a lowercase letter\nhas a special character")
    password = str(input("password: "))

  except ValueError:
    print("\nINVALID, Please try again\n")
    continue

  if len(password) <= 7:
    print("\nINVALID, Please try again. Too few characters\n")
    continue

  for x in range(len(password)):
    if password[x].isdigit() == True:
      digit = True

    elif password[x] >= chr(65) and password[x] <= chr(90):
      upper = True

    elif password[x] >= chr(97) and password[x] <= chr(122):
      lower = True

    elif (password[x] >= chr(32) and password[x] <= chr(47)) or (password[x] >= chr(58) and password[x] <= chr(64)) or (password[x] >= chr(91) and password[x] <= chr(96)) or (password[x] >= chr(123) and password[x] <= chr(126)):
      special = True

  if digit == True and upper == True and lower == True and special == True:
    print("Congrats your password meets all the requirements")
    break

  else:
    print("Password is invalid because")
    if digit == False:
      print("\nNo Numeric values found.")
    if upper == False:
      print("\nNo Uppercase letters found.")
    if lower == False:
      print("\nNo Lowercase letters found.")
    if special == False:
      print("\nNo Special letters found.")
    continue


#end of part 2

#start of part 3

#printing out a new line to make the console look more clean
print("\nPart 3")

#list to store all numbers that contain a three
part3List = []

#for loop that goes through each number from 1 - 1000
for n in range(1, 1001):
  #uses / and % to check and see if the number has a 3 in it 
  if n == 3 or n % 10 == 3 or (int((n / 10)) % 10 == 3) or int(n / 100) == 3:
    part3List.append(n)

for x in range(len(part3List)):
  print(part3List[x], '|', end=" ")
#end of part 3

#start of part 4

#printing out a new line to make the console look more clean
print("\n\nPart 4")

#list to store even numbers 1 - 100
part4List = []

#for loop that will fill the list from 1 - 100
#if it passes the if statement
for n in range(1, 101):
  #checks to see if the remainder is 0 so we know it is
  #an even number and adds it to the list
  if n % 2 == 0:
    #use the .append() method to easily add the
    #end of the list
    part4List.append(n)

#use .reverse() to flip the list
part4List.reverse()

#print out the reversed list
#starts from 100 and goes to 2
print(part4List)

#end of part 4

#start of part 5

#printing out a new line to make the console look more clean
print("\nPart 5")

#created a list to store all prime numbers 100-1000
part5List = []

#created my own function to check if a number is prime or not
#defining the function/method name and telling it what parameters to take
def isPrime(num):
  #hold value of 1 (is not prime) or 0 (is prime)
  #after the loop finishes the value is checked at the end to 
  #determin whether to output True or False
  prime = 0
  #checks to see if the number is 1 or negative
  if num > 1:
    #cycles through the range of 2 and the sqrt(number) + 1 
    #this means k will iterate starting at the value 2 all the way
    #up to sqrt(number) + 1
    #we use int() to cast to an int becasuse we dont want decimals
    #we are able to use the sqrt function bc we imported it form the math class
    for k in range(2, int(sqrt(num)) + 1):
      #gets the remainder of num
      if num % k == 0:
        #change prime variable to equal 1
        prime = 1
        #break out of if statement and contine the loop
        break
    #checks the value inside the prime variable
    if prime == 0:
      #returns a boolean value of True
      return True
    else:
      #returns a boolean value of False
      return False
  else:
    #returns a boolean value of False
    return False
        
#loop to start at 100 and finish at 1001
#x starts at 100 and iterates by 1 until 1000
for x in range(100, 1001):
  #calls the method we made isPrime to check and see if the value, x, is prime
  if isPrime(x) == True:
      #if it is prime we append it to our list
      part5List.append(x)
  #if it isnt prime we just continue the loop
  else:
    continue

#this just prints it nice and pretty like in part 3
for j in range(len(part5List)):
  print(part5List[j], '|', end=" ")

#end of part 5

#end of program