# practice question of for loop

# question ... Python program to check if a given number is an Armstrong number

give_number = int(input("Enter the number : "))

give_number= str(give_number) # convert number into string

string_length = len(give_number) # to find the length

sum = 0
for i in give_number:
    sum += int(i)**string_length
    
if sum == int(give_number):
    print("the given number is ", give_number, " is an amstrong number")
else:
    print("the given number is ", give_number, " is not amstrong number")