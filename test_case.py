import unittest
from Milestone import Courses, Student, University

class Test_Course(unittest.TestCase):
    def test_courses(self):     
        Ryan = Courses("CSE1010", 3, ["Johnny", "Michael", "Ryan"])
        self.assertEqual(Ryan.get_student_count(), 3)

if __name__ == '__main__':
    unittest.main()