# 1: Print the first 10 natural numbers using for loop.
for i in range (1,11):
    print(i)

# 2: Python program to print all the even numbers within the given range.

n= int(input("Enter the number"))
for i in range (1,n):
    if i%2==0:
        print ("That is even number : ",i)
    else:
        print("That should be odd number ", i)
        
# 3: Python program to calculate the sum of all numbers from 1 to a given number.

given_number= int(input("Enter the number"))
sum= 0
for i in range(1,given_number+1):
    sum +=i
    print(sum)

# 4:  Python program to calculate the sum of all the odd numbers within the given range.
given_number= int(input("Enter the number : "))
sum = 0

for i in range(1,given_number+1):
    if i%2!=0:
        sum+=i
        print(sum)

# 5:   Python program to print a multiplication table of a given number
give_number= int(input("Enter the number"))

for i in range(1,21):
    print(give_number, "x", i ,"=", give_number*i)

give_marks= int(input("Enter the number"))

if(give_marks>100):
    print("enter valid marks")
elif(100>=give_marks>90):
    print("A")
elif(90>give_marks>80):
    print("B")
elif(80>give_marks>70):
    print("C")
elif(70>give_marks>60):
    print("D")
elif(60>give_marks>50):
    print("E")
elif(50>give_marks>40):
    print("F")
else:
    print("fail")