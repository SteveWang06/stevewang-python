try:
	with open('input.Inp', 'r') as fileInp:
		ten = fileInp.readline().rstrip('\n')
		tuoiHienTai = int(fileInp.readline())
	pass
	with open('output.Out','w') as fileOut:
		fileOut.write('my name is {}, now my age is {} , after 10 year my age is {} '.format(ten, tuoiHienTai, tuoiHienTai + 10))
except FileNotFoundError:
	with open('output.Out', 'w') as fileOut:
		fileOut.write('can not find input file\nplease! make input file')
except:
	with open('output.Out', 'w') as fileOut:
		fileOut.write('data inside input file is invalid\nplease! fix data of input file')

	