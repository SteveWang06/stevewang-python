#cach lam tron so thap phan
a=float(input())
b=int(input())
print('{0:.{1}f}'.format(a,b))
print(round(a))

#cach lam tron so thap phan co xu ly dau vao
a=input('A number is ')
b=input('B number is ')
try:
	a=float(a)
	b=int(b)	
	print('{0:.{1}f}'.format(a,b))
except:
	print('input data is wrong, try again')
	
#khi su dung while thi khi nhap sai so chuong trinh se cho nhap lai	
while True:
	try:
		a=float(input("A number is "))
		break
	except:
		print('data type of A number is wrong, try again ') 
				
	pass

while True:
	try:
		b=int(input('B number is '))
		break
	except:
		print('data type of B number is wrong, try again')
		
	pass
print('{0:.{1}f}'.format(a,b))


