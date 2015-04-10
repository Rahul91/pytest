class Person:
	def set_details(self, name, age):
		self.name = name
		self.age = age

	def get_details(self):
		return self.name, self.age
		 

obj1 = Person()
obj2 = Person()

obj1.set_details("Rahul", 23)
obj2.set_details("Bittu", 26)

print obj1.get_details()
print obj2.get_details()


