age=int(input("enter ur age  "))
if (age<0 or age==0):
    print("u can't watch")
elif 0<age<=3:
    print("price is 0")
elif 3<age<=10:
    print("price is 50")
elif 10<age<=20:
    print("price is 100")
elif 20<age<=60:
    print("price is 150")        
else:
    print("price is 200")
