a=input("Enter main string: ")
b=input("Enter substring: ")
if(b in a):
    print(a.index(b))   
else:
    print(-1)