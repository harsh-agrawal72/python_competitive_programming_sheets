a = int(input("enter any number"))
if(a%5==0 and a%11==0):
    print("a is divisible by both 5 and 7")
elif(a%5==0):
    print("a is not divisible by 11 but divisible by 5")
elif(a%11==0):
    print("a is divisible by 11 but not divisible by 5")
elif(a<0):
    print("You entered wrong value")
else:
    print("a is not divisible by 11 and 5 both")