# 1
# name = input("What is your name?: \n")
# print("Hello " + name)

# 2
# x = 10 
# print(x)

#3
# personNumber = int(input("Choose any whole number: \n"))

# if personNumber > 10:
#   print("Your number is greater than 10")
# elif personNumber < 10:
#   print("Your number is less than 10")
# else:
#   print("Your number is 10")

#4
# personNumber2 = int(input("Choose any whole number: \n"))
# if personNumber2 % 2 == 0:
#   print("Even")
# else:
#   print("Odd")

#5
# list = ["France", "Belgium", "U.S.A", "China", "Russia"]
# for i in list:
#   print(i)

#6
# import random

# list2 = []

# for i in range(10):
#   list2.append(random.randint(1,100))
# print(list2)

#7
# import random
# list3 = []

# for i in range(10):
#   list3.append(random.randint(1,100))

# number = int(input("Please enter a number\n"))

# count = 0

# for e in list3:
#   if e < number:
#     count+=1

# print("{} numbers in the list are less than {}.".format(count, number))

#8
# while True:
#   word = input("Enter a word please: ")
#   if word == "Stop":
#     break
#   for letter in word:
#     print(letter)

#9


num_list = []

def calc_average():
  total=0
  for i in num_list:
    total+=i
  average = total/len(num_list)
  print(average)

while True:
  answer = input("Enter a number to keep going or type 'STOP' to calculate you current average.")

  if answer == "STOP":
    calc_average()
    break
  else:
    num_list.append(int(answer))


