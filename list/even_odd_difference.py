a = list(map(int,input("enter the number : ").split()))
even_count = 0
odd_count = 0
for i in a:
    if(i%2==0):
        even_count+=1
    else:
        odd_count+=1
difference = even_count-odd_count
if(difference<0):
    print(difference*-1)
else:
    print(difference)