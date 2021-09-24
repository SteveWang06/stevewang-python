'''
while True:
#tao dieu kien dau vao
    try:
        a=int(input('a is '))
        b=int(input('b is '))
        break
    except:
        print('input a and b again ')
pass

        #neu a lon hon b thi sao
if a>b :
    print('number a must be less than number b, try again')
    
elseif a==b :
    print('number a must be less than number b, try again')
    
       #cac truong hop con lai
else:
    tong=0   #tao bien tong
    i=a      #cho a chay tren day so i
    while i<=b:
        tong+=i  #cong don cac gia tri de tinh tong
        i+=1     #tang gia tri cua bien chay len 1 don vi
    print(tong)
'''



while True:
    try:
        a=int(input('a = '))
        b=int(input('b = '))
        if a<b :
            tong=0
            for i in range(a,b+1):
                tong+=i
            print(tong)
            break
        elif a==b:
            print('number a must be less than number b')
        else:
            print('number a must be less than number b')
    except:
        print('a and b wrong')



