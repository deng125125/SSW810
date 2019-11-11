"""
Test HW11
"""
import unittest
import sqlite3
from HW11_Xiaoxiao_Deng import Repository, Student


class TestRepository(unittest.TestCase):
    """ Test repository"""
    def setUp(self):
        self.test_path = "D:\\2019_Fall_Stevens\\ssw810\\homework\\HW11"
        self.rep = Repository(self.test_path)

    def test_info_major(self):
        """ test info_major"""
        expect = {'SFEN': {'required': ['SSW 540', 'SSW 810', 'SSW 555'],
                           'electives': ['CS 501', 'CS 546']},
                  'CS': {'required': ['CS 570', 'CS 546'],
                           'electives': ['SSW 810', 'SSW 565']}}
        self.assertEqual(self.rep.info_major, expect)

    def test_info_student(self):
        """ test info_student"""
        expect = {'10103': {'name': 'Jobs, S', 'dept': 'SFEN'},
                  '10115': {'name': 'Bezos, J', 'dept': 'SFEN'},
                  '10183': {'name': 'Musk, E', 'dept': 'SFEN'},
                  '11714': {'name': 'Gates, B', 'dept': 'CS'}}
        self.assertEqual(self.rep.info_student, expect)

        expect2 = {'10103': {'courses': ['CS 501', 'SSW 810'] , 'rr': ['SSW 540', 'SSW 555'], 're': 'None'},
                  '10115': {'courses': ['CS 546', 'SSW 810'] , 'rr': ['SSW 540', 'SSW 555'], 're': 'None'},
                  '10183': {'courses': ['SSW 555', 'SSW 810'] , 'rr': ['SSW 540'], 're': 'None'},
                  '11714': {'courses': ['CS 546', 'CS 570', 'SSW 810'], 'rr': 'None', 're': 'None'}}
        for cwid in self.rep.info_student:
            s = Student(cwid, self.test_path)
            self.assertEqual(s.courses, expect2[cwid]['courses'])
            self.assertEqual(s.remaining_required, expect2[cwid]['rr'])
            self.assertEqual(s.remaining_electives, expect2[cwid]['re'])

    def test_info_instructor(self):
        """ test info_instructor"""
        expect = {'98764': {'name': 'Cohen, R', 'dept': 'SFEN'},
                  '98763': {'name': 'Rowland, J', 'dept': 'SFEN'},
                  '98762': {'name': 'Hawking, S', 'dept': 'CS'}}
        self.assertEqual(self.rep.info_instructor, expect)

    def test_info_grade(self):
        """ test info_grade"""
        expect = [['10103', 'SSW 810', 'A-', '98763'], ['10103', 'CS 501', 'B', '98762'],
                  ['10115', 'SSW 810', 'A', '98763'], ['10115', 'CS 546', 'F', '98762'],
                  ['10183', 'SSW 555', 'A', '98763'], ['10183', 'SSW 810', 'A', '98763'],
                  ['11714', 'SSW 810', 'B-', '98763'], ['11714', 'CS 546', 'A', '98764'],
                  ['11714', 'CS 570', 'A-', '98762']]
        self.assertEqual(self.rep.info_grade, expect)

    def test_instructor_table_db(self):
        """ test instructor_table_db"""
        db_path = "D://2019_Fall_Stevens\ssw810\homework\HW11\810_startup.db"
        db = sqlite3.connect(db_path)
        query = "select CWID, Instructor, Dept, Course, count(*) as Students " \
                "from instructors join grades on CWID=InstructorCWID group by Course"

        the_list = list()
        for row in db.execute(query):
            the_list.append(row)

        expect = [('98764', 'Feynman, R', 'SFEN', 'CS 501', 1), ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1),
                  ('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3), ('98763', 'Newton, I', 'SFEN', 'SSW 555', 1),
                  ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3), ('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4),
                  ('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3), ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1),
                  ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2), ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1),
                  ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1), ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1)]

        self.assertEqual(the_list, expect)





if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

