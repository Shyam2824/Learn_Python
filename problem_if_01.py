marks_1=int(input("Enter marks 1: "))
marks_2=int(input("Enter marks 2: "))
marks_3=int(input("Enter marks 3: "))

total_per= (100 *(marks_1 + marks_2 + marks_3))/300

if(total_per >= 33 and marks_1>=33 and marks_2>=33 and marks_3>=33):
    print("You are pass " ,total_per)
    
else:
    print("You are failed ", total_per)