from people import *

def main():
  aPerson = Person("Dave")
  aPerson.introduceSelf()

  aTeacher = Teacher("Mr Andy", "Computer Science")
  aTeacher.introduceSelf()
  aTeacher.teachingSubject()   

  aStudent = Student("Sally", 2023)
  aStudent.introduceSelf()
  aStudent.graduationYear()

if __name__ == "__main__":
  main()
