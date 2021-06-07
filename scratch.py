class Dog:
	def __init__(self,name, age):
		self.name = name
		self.age = age

	def get_name(self, name):
		return self.name
	
	def get_age(self):
		return self.age
	
	def set_age(self, age):
		self.age = age

d1_age = 23
d2_name = "Tom"
d = Dog(d2_name,d1_age)
print(d.get_age())