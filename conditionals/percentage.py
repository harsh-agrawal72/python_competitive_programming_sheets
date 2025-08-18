percentage = int(input("enter your percentage"))
if(percentage>90):
    print("Grade is A")
elif(percentage>80 and percentage<90):
    print("Grade is B")
elif(percentage>70 and percentage<80):
    print("Grade is C")
elif(percentage>60 and percentage<70):
    print("Grade is D")
elif(percentage<0):
    print("Wrong Percentage")
else:
    print("Fail")