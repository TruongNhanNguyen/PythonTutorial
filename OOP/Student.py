class Student:
	def __init__(self, name, age, grade):
		self._name = name
		self._age = age
		self._grade = grade

	def getGrade(self):
		return self._grade

	def getName(self):
		return self._name

	def getAge(self):
		return self._age


class Course:
	def __init__(self, name, maxStudent):
		self._name = name
		self._maxStudent = maxStudent
		self._studentsList = []

	def getName(self):
		return self._name

	def addStudent(self, student):
		if len(self._studentsList) < self._maxStudent:
		    self._studentsList.append(student)
	
	def getAverageGrade(self):
		avarageGrade = 0
		for student in self._studentsList:
			avarageGrade += student.getGrade()
		return avarageGrade / len(self._studentsList)

s1 = Student("Nhan", 19, 100)
s2 = Student("Dang", 19, 95)
s3 = Student("Nguyen", 19, 90)
s4 = Student("Kien", 19, 85)

course = Course("Datastructure and Algorithm", 100)
course.addStudent(s1)
course.addStudent(s2)
course.addStudent(s3)
course.addStudent(s4)

print("Course's name: ", course.getName())
print("Student 1: ", s1.getName(), s1.getAge(), s1.getGrade())
print("Student 2: ", s2.getName(), s2.getAge(), s2.getGrade())
print("Student 3: ", s3.getName(), s3.getAge(), s3.getGrade())
print("Student 5: ", s4.getName(), s4.getAge(), s4.getGrade())
print("Average grade of course: ", course.getAverageGrade())