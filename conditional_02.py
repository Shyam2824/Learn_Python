num1= int(input("Enter your number 1: "))
num2= int(input("Enter your number 2: "))
num3= int(input("Enter your number 3: "))
num4= int(input("Enter your number 4: "))

if(num1 > num2 and num1 > num3 and num1 > num4 ):
    print("Num1 is greater")
    
elif(num2 > num1 and num2 > num3 and num2 > num4):
    print("Num2 is greater")
    
elif(num3 > num1 and num3 > num2 and num3 > num4):
    print("Num3 is greater")
    
else:
    print("Num4 is greater")