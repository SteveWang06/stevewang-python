import re

str = 'BaiTapFlag'
match = re.match(r'[A-z0-9]', str)
if match:                   
    print('true!');
else:
    print ('false!')


#I hoặc IGNORECASE - Không phân biệt hoa thường khi so khớp.
#L hoặc LOCALE - So Khớp với local hiện tại.
#M hoặc MULTILINE - Thay đổi $ và ^ thành kết thúc của một dòng và bắt đầu của một dòng thay vì mặc định là kết thúc chuỗi và bắt đầu chuỗi.
#A hoặc ACSII - Thay đổi \w, \W, \b, \B, \d, \D, \S và \s thành so khơp full unicode.
#S hoặc DOTALL -Thay đổi pattern . thành khớp với bất kỳ ký tự nào và dòng mới.