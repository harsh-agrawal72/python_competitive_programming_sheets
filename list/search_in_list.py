a = list(map(int,input("enter the number : ").split()))
digit = int(input())
for i in a:
    if digit==i:
        print(digit+"is present in list")