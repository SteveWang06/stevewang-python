#cong day so khong lien tuc
a= input()
#Su dung ham split() de cat day gia tri thanh cac chuoi con
b= a.split()
#Su dung ham map() de thuc hien viec chuyen cac chuoi con sang kieu so nguyen
c= map(float,b)
d= sum(c)
print(d)

a=input()
b=[float(i) for i in a.split()]
c=sum(b)
print(c)

#cong day so lien tuc
a=input()
b=input()
c=float(float(a)*(float(b)+float(a)))/2
print(c)