num = int(input("enter any number: "))
count=0
new = 1
num1=str(num)
is_palindrome= True
while(count<len(num1)):
    if(num1[count]==num1[len(num1)-new]):
        count+=1
        new+=1
    else:
        is_palindrome=False
        break

if(is_palindrome==True):
    print("Your number is a palindrome number")
else:
    print("Your number is not a palindrome number")