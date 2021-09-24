while True:
    try:
        a,b,c=map(float,input('nhap abc' ).split())
        assert a>=0 and b>=0 and c>=0
        if a+b>c and a+c>b and b+c>a:
            print('{a}, {b}, {c} la ba canh cua tam giac')
            break
        else:
            print('{a}, {b}, {c} khong phai la ba canh cua tam giac')
            break
    except ValueError:
        print('nhap sai,xin nhap lai')
    except AssertionError:
        print('canh la so duong')



