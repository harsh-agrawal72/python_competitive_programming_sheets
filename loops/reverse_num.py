num = int(input("enter any number"))
# num1 = []
ans = 0
while num >0:
        digit=num%10
        # num1.append(digit)
        num=num//10
        ans = ans * 10 + digit
# for i in num1:
        # print(i, end="")
print(ans)
        