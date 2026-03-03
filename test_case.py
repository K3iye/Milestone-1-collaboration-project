import unittest
from Milestone import Courses, Student, University

class Test_University(unittest.TestCase):
    """
    Created by: Johnny
    
    Tests for the University class methods verifies object creation,
    adding/retrieving students and courses, duplicates, and enrollment functions
    """
    def test_object_creation(self):
        """
        Test that a University object initializes with empty dictonary
        """
        uconn = University()
        self.assertIsInstance(uconn, University)
        self.assertEqual(uconn.students, {})
        self.assertEqual(uconn.courses, {})
        
        
    def test_addcourse(self):
        """
        Test adding a course to the university
        """
        uconn = University()
        course = uconn.add_course("CSE2050", 2)
        
        self.assertIn("CSE2050", uconn.courses) # Checks if the string is in the courses dict
        self.assertEqual(course.credits, 2)

    def test_addstudent(self):
        """
        Test adding a student to the university
        """
        uconn = University()
        student = uconn.add_student("STU00201", "Johnny")
        
        self.assertIn("STU00201", uconn.students)
        self.assertEqual(student.name, "Johnny")

    def test_getstudent(self):
        """
        Test retrieving a student using their ID.
        """
        uconn = University()
        uconn.add_student("STU00201", "Johnny")
        student = uconn.get_student("STU00201")
        
        self.assertEqual(student.name, "Johnny")
        self.assertEqual(uconn.get_student("STU10000"), None)

    def test_getcourse(self):
        """
        Test retrieving a course by course_code.
        """
        uconn = University()
        uconn.add_course("CSE2050", 2)
        course = uconn.get_course("CSE2050")
        
        self.assertEqual(course.course, "CSE2050")
        self.assertEqual(course.credits, 2)
        self.assertEqual(uconn.get_course("CSE1010"), None)
        
    def test_get_course_enrollment(self):
        """
        Test that enrollment count shows the number of students added.
        """
        uconn = University()
        course = uconn.add_course("CSE2050", 2)
        student1 = uconn.add_student("STU00001", "Johnny")
        student2 = uconn.add_student("STU00002", "Ryan")
        course.add_student(student1)
        course.add_student(student2)
        self.assertEqual(course.get_student_count(), 2)
        
    def test_students_in_course(self):
        """
        Test retrieving list of students enrolled in a course.
        """
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

class Test_Course(unittest.TestCase):
    def test_courses(self):     
        Ryan = Courses("CSE1010", 3, ["Johnny", "Michael", "Ryan"])
        self.assertEqual(Ryan.get_student_count(), 3)

if __name__ == '__main__':
    unittest.main()