num = int(input("enter any number"))
if(num%3==0 and num%10==4):
    print("num is divisible by 3 and last digit is 4")
elif(num%3==0):
    print("num last digit is not 4")
elif(num%3!=0 and num%10!=4):
    print("num is not divisible by 3 and last digit is not 4")
else:
    print("num is not divisible by 3")