num = int(input("enter any number: "))
sum = 0
if num == 0:
    sum=0
    print("sum of digit is: ", sum)
elif(num<0):
    print("you entered negative value")
else:
    while num >0:
        digit=num%10
        num=num//10
        sum+=digit
    print("sum of digit is: ", sum)