import unittest
from Milestone import Courses, Student, University

class Test_Course(unittest.TestCase):
    def test_course_creation(self):
        ryan_courses = Courses("CSE1010", 3, ["Johnny", "Michael", "Ryan"])
        self.assertEqual(type(ryan_courses), Courses)

    def test_studentadd(self):
        michael_courses = Courses("CSE1010", 3, ["Johnny", "Michael", "Ryan"])
        michael_courses.add_student("Mobeen")
        self.assertIn("Mobeen", michael_courses.students)
    
    def test_duplicates(self):
        """
        Test duplicate values
        """
        ryan_courses = Courses("CSE1010", 3, ["Johnny", "Michael", "Ryan"])
        with self.assertRaises(ValueError):
            ryan_courses.add_student("Johnny")
    
    def test_studentcount(self):     
        Ryan = Courses("CSE1010", 3, ["Johnny", "Michael", "Ryan"])
        self.assertEqual(Ryan.get_student_count(), 3)

class Test_Student(unittest.TestCase):
    def test_student_creation(self):
        ryan = Student("STU20000", "Ryan", {"CSE1010":"A", "CSE2050": "B+"})
        self.assertEqual(type(ryan), Student)

    def test_enroll(self):
        ryan = Student("STU20000", "Ryan", {"CSE1010":"A", "CSE2050": "B+"})
        ryan.enroll("CSE3100", "B-")
        self.assertIn("CSE3100", ryan.student_courses)
    
    def test_gpa(self):
        ryan = Student("STU20000", "Ryan", {"CSE1010":"A"})
        self.assertEqual(ryan.calculate_gpa(), '4.00')
    
    def test_get_studentcourses(self):
        ryan = Student("STU20000", "Ryan", {"CSE1010":"A"})
        self.assertEqual(ryan.student_courses, ["CSE1010"])

class Test_University(unittest.TestCase):
    def test_addcourse(self):
        uconn = University()
        course = uconn.add_course("CSE2050", 2)
        
        self.assertIn("CSE2050", uconn.courses) # Checks if the string is in the courses dict
        self.assertEqual(course.credits, 2)
    
    def test_duplicate_course(self):
        """
        Test duplicate course values
        """
        uconn = University()
        course = uconn.add_course("CSE2050", 2)

        with self.assertRaises(ValueError):
            course2 = uconn.add_course("CSE2050", 2)

    def test_addstudent(self):
        uconn = University()
        student = uconn.add_student("STU00201", "Johnny")
        
        self.assertIn("STU00201", uconn.students)
        self.assertEqual(student.name, "Johnny")
    
    def test_duplicatestudent(self): 
        """
        Test duplicate student values
        """
        uconn = University()
        student = uconn.add_student("STU00201", "Johnny")

        with self.assertRaises(ValueError):
            student2 = uconn.add_student("STU00201", "Johnny")

    def test_getstudent(self):
        uconn = University()
        uconn.add_student("STU00201", "Johnny")
        student = uconn.get_student("STU00201")
        
        self.assertEqual(student.name, "Johnny")

        with self.assertRaises(ValueError):
            uconn.get_student("STU10000")

    def test_student_nonexistent(self):
        """
        Test if student is in the roster else raise error
        """
        uconn = University()
        uconn.add_student("STU00201", "Johnny")

        with self.assertRaises(ValueError):
            student = uconn.get_student("202")

    def test_getcourse(self):
        uconn = University()
        uconn.add_course("CSE2050", 2)
        course = uconn.get_course("CSE2050")
        
        self.assertEqual(course.course, "CSE2050")
        self.assertEqual(course.credits, 2)

    def test_course_nonexistent(self):
        """
        Test if course is in the roster else raise error
        """
        uconn = University()
        uconn.add_course("CSE2050", 2)
        with self.assertRaises(ValueError):
            uconn.get_course("CSE1010")

    def test_get_course_enrollment(self):
        uconn = University()
        course = uconn.add_course("CSE2050", 2)
        student1 = uconn.add_student("STU00001", "Johnny")
        student2 = uconn.add_student("STU00002", "Ryan")
        course.add_student(student1)
        course.add_student(student2)
        self.assertEqual(course.get_student_count(), 2)
        
    def test_students_in_course(self):
        uconn = University()
        course = uconn.add_course("CSE2050", 2)
        student1 = uconn.add_student("STU00001", "Johnny")
        student2 = uconn.add_student("STU00002", "Ryan")
        course.add_student(student1)
        course.add_student(student2)
        students = uconn.get_students_in_course("CSE2050")
        
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0].name, "Johnny")
        self.assertEqual(students[1].name, "Ryan")
        self.assertEqual(uconn.get_students_in_course("CSE1010"), None)

if __name__ == '__main__':
    unittest.main()