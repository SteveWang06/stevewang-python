import math
a=float(input('a = '))
b=float(input('b = '))
c=float(input('c = '))
if a == 0:
   if b == 0:
       if c == 0:
           print("Phuong trinh co vo so nghiem")
       else:
           print ("Phuong trinh vo nghiem")
   else:
       print ("Phuong trinh co mot nghiem duy nhat: \nx = {}".format(-c / b))
else:
    d=b*b-4*a*c
    if d==0:
        print('phuong trinh co nghiem kep')
        x1=x2=(-b)/(2*a)
        print('x1 = x2 =',x1)
    elif d>0:
        x1=float((-b+math.sqrt(d))/(2*a))
        x2=float((-b-math.sqrt(d))/(2*a))
        print('x1 =',round(x1,2))
        print('x2 =',round(x2,2))
    else:
        print('phuong trinh vo nghiem')
