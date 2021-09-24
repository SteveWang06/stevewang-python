while True:
	try:
		nameA=str(input('nameA : '))
		heightA=int(input('heightA : '))
		break
	except:
		print('data is Not True\nPlease fill in again')
	pass
while True:
	try:
		nameB=str(input('nameB : '))
		heightB=int(input('heightB : '))
		break
	except:
		print('data is Not True\nPlease fill in again')
	pass
if heightA>heightB:
	print('{} is taller than {}'.format(nameA,nameB))
elif heightA==heightB:
	print('{} is as tall as {}'.format(nameA,nameB))
else:
	print('{} is shorter than {}'.format(nameA,nameB))