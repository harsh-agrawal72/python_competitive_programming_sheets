a=input("Enter the word: ")
b=int(input("Enter the ascii value: "))
found=0
for i in range(len(a)):
    if(ord(a[i])==b):
        found=i
        break
if(found==0):
    print("It doesn't exist")
else:
    print(found)
