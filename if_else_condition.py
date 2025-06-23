#calculate the temperature input taken from user
temp= float(input("Enter the temperature "))
if temp <= 15:
    print("temperature is not convinient ")
if 24 <= temp <= 28:
    print("temperature is convinient ")
    
# # age to election or elegible to vote
age=float(input("Enter your age"))
if age>=18:
    print("you are elegible to vote")
else:
    print("you are not elegible to vote")

# net salary
base_salary= float(input("Enter your base salary"))
year_service= int(input("Enter your year of service"))

if year_service>5:
    total_salary= base_salary + (0.08*base_salary) - (0.12*base_salary)
    print("You will get net salary " , total_salary)
else:
    net_salary= base_salary-(0.12*base_salary)
    print("you will get net salary ", net_salary)