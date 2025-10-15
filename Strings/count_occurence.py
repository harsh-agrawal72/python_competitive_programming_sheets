a=input("Enter the string: ")
b=input("Enter the substring to find its occurrence: ")
count=0
if b in a:
    for i in range((len(a)-len(b))+1):
        if a[i:i+len(b)]==b:
            count+=1
    print(count)
else:
    print("The substring is not present in the string")