# WAP to even number between 1 &50

num =1
while num<=50:
    if num%2 ==0:
        print(num)
    num= num+1


######## valid mail id

email = input("Enter your Mail Id  :  ")
valid_mail= False

while not valid_mail:
    if "@" in email and "." in email:
        print("your mail id is valid")
        
        valid_mail = True
    
    else:
        print("your mail id not valid, try again")
        
        email= input("please enter your mail id")