n = int(input())
for i in range(1,n+1):
    line = ""
    for j in range(1, i+1):
        line = '{} {}'.format(line , j)
    print(line)