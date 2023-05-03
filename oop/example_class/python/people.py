class Person:
  def __init__(self, name):
    self.name = name

  def introduceSelf(self):
    print(f"Hi my name is {self.name}.")

class Teacher(Person):
  def __init__(self, name, subject):
    super().__init__(name)
    self.subject = subject

  def teachingSubject(self):
    print(f"I teach {self.subject}.")

class Student(Person):
  def __init__(self, name, year):
    super().__init__(name)
    self.year = year
	
  def graduationYear(self):
    print(f"I will graduate in {str(self.year)}.")
