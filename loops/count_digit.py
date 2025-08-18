num = int(input("enter any number: "))
count = 0
if num == 0:
    count=1
    print("Number of digit is: ", count)
elif(num<0):
    print("you entered negative value")
else:
    while num >0:
        num//=10
        count+=1
    print("Number of digit is: ", count)