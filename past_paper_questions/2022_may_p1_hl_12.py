import random

name = ['James', 'Edgar', 'Andy', 'Phil', 'Gilly']
grade = []
mark = []
for i in range(5):
  mark.append(random.randint(0,100))

'''
loop N from 0 to len(MARKS) // 30

  if MARK[N] >= 80 then
    GRADE.addValue("Distinction")
  else if MARK >= 60 then
    GRADE.addValue("Merit")
  else if MARK >= 40 then
    GRADE.addValue("Pass")
  else
    GRADE.addValue("Fail")
  end if
'''

for n in mark:
  if n >= 80:
    grade.append("Distinction")
  if n >= 60:
    grade.append("Merit")
  if n >= 40:
    grade.append("Pass")
  else:
    grade.append("Fail")

'''
Construct an algorithm using pseudocode to output the names and grades
of all students who achieve a grade of Merit or Distinction.

loop N from 0 to len(MARK) // 30
  if MARK[N] >= 60
    output NAME[N], GRADE[N]
'''

for n in range(len(mark)):
  if mark[n] >= 60:
    print(name[n], grade[n])
