distance = int(input("Enter the distance : "))

if distance<=3:
    transport = "walk"
elif distance <=50:
    transport= "Bike"
else :
    transport= "car"
print(transport)