angle_1 = int(input("enter first angle"))
angle_2 = int(input("enter second angle"))
angle_3 = int(input("enter third angle"))
sum_of_angle = angle_1+angle_2+angle_3
if(sum_of_angle==180):
    print("Triangle is valid")
else:
    print("Triangle is invalid")