import csv

#------------------------------ Things to ADD ---------------------------
""" 
    - Make test cases for course class and Student class

    - Look at the code for course_data_to_dict function

    - Make Error handling for the specific things stated on the Milestone pdf
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
    university_dict = {}

    with open(filename, "r", newline = '') as csv_file:
        my_reader = csv.DictReader(csv_file)
        for row in my_reader:
            student_id = row['student_id'] # takes in the student_id and its row
            name = row['name'] # gets the name of whats in that student_id's row
            courses = row['courses'] # gets the course of whats in that student_id's row
            courses_dict = {} # make a dictionary for the courses
            course_pairs = courses.split(";")
            for pair in course_pairs: 
                course, grade = pair.split(":") #splits course as key and grade as value inside of the dict
                courses_dict[course] = grade

            university_dict[student_id] = { #when inputted a student_id gives out the name and courses which values are courses_dict
                "name": name,
                "courses": courses_dict
        }
    return university_dict

course_data = course_data_to_dict('course_catalog.csv')
university_data = university_data_to_dict('university_data.csv')
#print(university_data["STU00001"]) # -> is formatted like this 
                                    #      'name': Student_1
                                    #      'courses': {
                                    #      'Math2010': 'C+ 
                                    #       }

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
    
    def get_courses(self):
        return self.student_courses
    
    def get_course_info(self):
        return f"{self.name} has taken {self.student_courses}, and has these grades {self.student_grades}, these classes accumulate to {self.total_cred} credits."   

class University:
    def __init__(self):
        # Student Object
        self.students = {}
        
        #Course Object
        self.courses = {}
        
    def add_course(self, course_code: str, credits: int) -> Courses:  # Course object 
        if course_code in self.courses:
            return self.courses[course_code]
        
        new_course = Courses(course_code, credits, [])
        self.courses[course_code] = new_course
        return new_course

    def add_student(self, student_id: str, name: str) -> Student: # Student object 
        if student_id in self.students:
            return self.students[student_id]
        
        new_student = Student(student_id, name, {})
        self.students[student_id] = new_student
        return new_student
    
    def get_student(self, student_id: str) -> Student | None: #Student Object or None
        if student_id in self.students:
            return self.students[student_id]
        return None

    def get_course(self, course_code: str) -> Courses | None: # Course object or None
        if course_code in self.courses:
            return self.courses[course_code]
        return None
    
    def get_course_enrollment(self, course_code: str) -> int:
        student_count = self.courses[course_code].get_student_count()
        return student_count
    
    def get_students_in_course(self, course_code: str) -> list[Student] | None: # List of student objects or None if course doesn't exist
        if course_code in self.courses:
            return self.courses[course_code].students
        return None
    
# ---------------------------------- SIMPLE TESTS -----------------------------------                    
# ryan = Student("100101", "Ryan", {"CSE1010":"A", "CSE2050": "B+"})
# ryan_courses = Courses("CSE1010", 3, ["Johnny", "Michael", "Ryan"])
# ryan.enroll("CSE3100", "B-")
# print(ryan.calculate_gpa())
# print(ryan.get_courses())
# print(ryan.get_course_info())

# harry = Student("304405", "Harry", {"CHEM1010": "A", "ENG1010": "A-", "BIO1010": "A"})
# print(harry.calculate_gpa()

Uconn = University()

course = Uconn.add_course("CSE2050", 2)
Student1 = Uconn.add_student("STU10000", "Johnny")
Student2 = Uconn.add_student("STU10001", "Ryan")

course.add_student(Student1)
course.add_student(Student2)
students = Uconn.get_students_in_course("CSE2050")
# student = Uconn.get_student("STU10000")


# print(course.credits)
# print(Uconn.students)
# print(student.name)
# print(course.get_student_count())
# print(students[0].name)
