word= input()
b = word.split()
c = b[::-1]
print(c)
for i in c:
        d = i[::-1]
        print(d,end="")