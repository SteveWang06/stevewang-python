#cach lam tron so thap phan
a=float(input())
b=int(input())
print('{0:.{1}f}'.format(a,b))
print(round(a))

#cach lam tron so thap phan co xu ly dau vao
a=input('so a la ')
b=input('so b la ')
try:
	a=float(a)
	b=int(b)	
	print('{0:.{1}f}'.format(a,b))
except:
	print('nhap sai gia tri')
	
#khi su dung while thi khi nhap sai so chuong trinh se cho nhap lai	
while True:
	try:
		a=float(input("a la "))
		break
	except:
		print('ban da nhap sai so a') 
		
		
	pass
while True:
	try:
		b=int(input('b la '))
		break
	except:
		print('ban da nhap sai so b')
		
	pass
print('{0:.{1}f}'.format(a,b))


