import math

a=float(input("nhap a: "))
b=float(input("nhap b: "))
c=float(input("nhap c: "))

if a==0:
    if b==0:
        if c==0:
            print("Phuong trinh co vo so nghiem")
        else:
         print("Phuong trinh vo nghiem")
    else:
      print("Phuong trinh bac nhat, nghiem x=",-c/b)
else:
    delta=b**2-4*a*c
    
    if delta<0:
        print("Phuong trinh vo nghiem (delta <0)")
    elif delta ==0:
        x = -b / (2*a)
        print("Phuong trinh co nghiem kep x =", x)
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        print("Phuong trinh co hai nghiem phan biet:")
        print("x1=",x1)
        print("x2=",x2)
