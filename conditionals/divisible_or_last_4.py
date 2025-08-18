num = int(input("enter any number"))
if(num%3==0 or num%10==4):
    print("num is divisible by 3 or last digit is 4")
elif(num%3!=0 and num%10!=4):
    print("num is not divisible by 3 and last digit is not 4")
else:
    print("You entered a wrong number")