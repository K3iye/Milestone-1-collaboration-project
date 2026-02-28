import csv

#------------------------------ Things to ADD ---------------------------
"""
    - Finish Task 3: Create the functions of the University Class
    
    - Make more test cases on the test_Case.py

    - Look at the code for course_data_to_dict function and help with
    organizing the university_data_to_dict (idk how to organize all that data)

    - university_data_to_dict function important for university class later and better
    for organizing 
"""
def course_data_to_dict(filename):
    course_dict = {}

    with open(filename, "r", newline = '') as csv_file:
        my_reader = csv.reader(csv_file)
        next(my_reader)
        for row in my_reader:
            course_code = str(row[0])
            credits = int(row[1])
            course_dict[course_code] = credits
        return course_dict
    
def university_data_to_dict(filename):
    university_dict = []

    with open(filename, "r", newline = '') as csv_file:
        my_reader = csv.DictReader(csv_file)
        for row in my_reader:
            university_dict.append(row)
        return university_dict

course_data = course_data_to_dict('course_catalog.csv')
university_data = university_data_to_dict('university_data.csv')

class Courses: 
    # students is a list of Student objects. students entrolled in the course
    def __init__(self, course_code: str, credits: int, students: list):
        self.course = course_code
        self.credits = credits
        self.students = students
    
    # Supposed to add a Student object to the course roster    
    def add_student(self, student):
        self.students.append(student)
   
   # returns the number of students currently enrolled 
    def get_student_count(self) -> int:
        return len(self.students)
    

class Student:
    def __init__(self,student_id: str, name: str, courses: dict):
        self.student_id = student_id
        self.name = name
        #courses is a dictionary of courses a student has taken Course: grade "A", "B+"
        self.courses = courses
        self.student_courses = []
        for key in self.courses:
            self.student_courses.append(key)
    
    def enroll(self, course: str, grade: str):
        self.courses[course] = grade
        self.student_courses.append(course)
        
    def update_grade(self,course: str,grade: str):
        self.courses[course] = grade
    
    def calculate_gpa(self):
        total_gpa = 0
        student_cred = []
        self.student_grades = []
        self.student_gpanum = []
        grade_point = {
        'A' : 4.0, 'A-' : 3.7,
        'B+': 3.3, 'B' : 3.0, 'B-' : 2.7,
        'C+': 2.3, 'C' : 2.0, 'C-' : 1.7,
        'D' : 1.0,
        'F' : 0.0
        }
    
        for value in self.courses.values():
            self.student_grades.append(value)
        
        for grade in self.student_grades:    
            if grade in grade_point:
                self.student_gpanum.append(grade_point[grade])
    
        for item in self.student_courses:
            if item in course_data:
                student_cred.append(course_data[item]) # gives all the credits

        self.total_cred = sum(student_cred)
        
        for i in range(len(self.student_gpanum)):
            total_gpa = total_gpa + (self.student_gpanum[i] * student_cred[i])
        total_gpa /= self.total_cred
        return f"{total_gpa:.2f}"
    
    #-------------------- CANNOT CALCULATE GRADE WITHOUT CSV FILE INFORMATION (CREDITS) ------------------------ 
    def get_courses(self):
        return self.student_courses
    
    def get_course_info(self):
        return f"{self.name} has taken {self.student_courses}, and has these grades {self.student_grades}, these classes accumulate to {self.total_cred} credits."    
    
class University:
    def __init__(self, students: dict, courses: dict):
        self.students = students
        self.courses = courses

ryan = Student("100101", "Ryan", {"CSE1010":"A", "CSE2050": "B+"})
ryan_courses = Courses("CSE1010", 3, ["Johnny", "Michael", "Ryan"])
ryan.enroll("CSE3100", "B-")
print(ryan.calculate_gpa())
print(ryan.get_courses())
print(ryan.get_course_info())

harry = Student("304405", "Harry", {"CHEM1010": "A", "ENG1010": "A-", "BIO1010": "A"})
print(harry.calculate_gpa())
