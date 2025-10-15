a=input()
b = a + a 
result = ""
for i in range(len(b)):
    if(b[i].isupper()):
        continue
    elif(b[i] in {'a','e','i','o','u'}):
        result+="#"
    else:
        result+=b[i]
print(result)