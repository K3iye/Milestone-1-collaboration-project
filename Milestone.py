import csv

#------------------------------ Things to ADD ---------------------------
    """
    -Fix self.student courses or find another way to get that information throughout
    the class to get course_info output and calculate gpa.
    
    -Finish TASK 3 (pretty general cause we havent started yet)
    
    -Make testing on the test_Case.py using unnittest
    """




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
    
    def enroll(self, course: str, grade: str):
        self.courses[course] = grade
        
    def update_grade(self,course: str,grade: str):
        self.courses[course] = grade
    
    def calculate_gpa(self):
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
        return self.student_gpanum
    
        """
        total_gpa = 0
        student_cred = []
        for item in self.student_courses:
            if item in (whereever we store the csv with the courses):
                student_cred.append(csvfile.value[item]) # gives all the credits

        total_cred = sum(student_cred)
        
        for i in len(student_gpa):
            total_gpa = total_gpa + (student_gpa[i] * student_cred[i])
        total_gpa /= total_cred
        """
    
    #-------------------- CANNOT CALCULATE GRADE WITHOUT CSV FILE INFORMATION (CREDITS) ------------------------
        
        
    def get_courses(self) -> list:
        self.student_courses = []
        for key in self.courses:
            self.student_courses.append(key)
        return self.student_courses
    
    
    def get_course_info(self):
        return f"{self.name} has taken placeholder, and has these grades {self.student_grades}, these classes accumulate to placeholder credits."    
            
ryan = Student("100101", "Ryan", {"CSE1010":"A"})
ryan_courses = Courses("CSE1010", 3, ["Johnny", "Michael", "Ryan"])
print(ryan.calculate_gpa())
print(ryan.get_course_info())
