score= int(input("Enter the score : "))

if score>100:
    grade="not exist"
elif score>90:
    grade= "A"
elif score>80:
    grade= "B"
elif score>70:
    grade= "C"
elif score>60:
    grade= "D"
else:
    grade= "F"
print ("This is your Grade :", grade)