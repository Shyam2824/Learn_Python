number = [1, -5, -15,6, 7, 10, -18, -100, -86]
count_positive_number=0
count_negative_number =0

for num in number : 
    if num >0: 
        count_positive_number +=1
    else :
        count_negative_number+=1
print("Final positive number is : " , count_positive_number)
print("Final positive number is : " , count_negative_number)