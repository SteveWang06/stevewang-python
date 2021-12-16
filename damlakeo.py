import random
import numpy

choose = ['石頭','剪刀','布']
result = ['draw', 'lose', 'win']
playLaw = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]
machineChoose = numpy.random.randint(3)
playerChoose = choose.index(input('enter your choose: '))
print('machine choose: %s \nyour choose: %s \nresult: %s \n' % (choose[machineChoose], choose[playerChoose], result[playLaw[machineChoose][playerChoose]]))