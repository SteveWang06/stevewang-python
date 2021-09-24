class Person:
	def __init__(self, name, birthday, gender, citizenship, marital_status):

		print('CURRICULUM VITAE OF VUONG GIA BAO')
		self.name, self.birthday, self.gender, self.citizenship, self.marital_status = name, birthday, gender, citizenship, marital_status

	def getName(self):
		print("Name: %s" %(self.name))
	
	def getBirthday(self):
		print("Birthday: %s" %(self.birthday))
	
	def getGender(self):
		print("Gender: %s" %(self.gender))

	def getCitizenship(self):
		print("Citizenship: %s" %(self.citizenship))

	def getMarital_status(self):
		print("Marital status: %s" %(self.marital_status))

person = Person('VUONG GIA BAO', 'june 13 2000', 'Male', 'VietNam', 'Single')
person.getName()
person.getBirthday()
person.getGender()
person.getCitizenship()
person.getMarital_status()