from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, yob: int):
        self.name = name
        self.yob = yob
        
    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.grade = grade
        
    def describe(self):
        print(f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.subject = subject
        
    def describe(self):
        print(f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")

class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self.specialist = specialist
        
    def describe(self):
        print(f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")

class Ward:
    def __init__(self, name: str):
        self.name = name
        self.people = []
        
    def add_person(self, person):
        self.people.append(person)
        
    def describe(self):
        print(f"Ward - Name: {self.name}")
        for person in self.people:
            person.describe()
            
    def count_doctor(self):
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1
        return count
    
    def sort_age(self):
        self.people.sort(key=lambda x: x.yob, reverse=True)
        
    # Get average yob of teachers
    def compute_average(self):
        sum_yob = 0
        count = 0
        for person in self.people:
            if isinstance(person, Teacher):
                sum_yob += person.yob
                count += 1
        return sum_yob / count
            
            
 # Examples
 # 2(a)
student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()
 
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()
 
 # 2(b)
print()
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# 2(c)
print(f"\nNumber of doctors in the ward: {ward1.count_doctor()}")

# 2(d)
print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

# 2(e)
print(f"\nAverage YoB of teachers in Ward1: {ward1.compute_average()}")

