"""
Test HW10
"""
import unittest
import os
from HW10_Xiaoxiao_Deng import Repository
from collections import defaultdict


class TestRepository(unittest.TestCase):
    """ Test repository"""
    def setUp(self):
        self.test_path = os.path.dirname(os.path.abspath(__file__)) + "\\HW10"
        self.rep = Repository(self.test_path)

    def test_info_major(self):
        expect = {'SFEN': {'required': ['SSW 540', 'SSW 564', 'SSW 555', 'SSW 567'],
                           'electives': ['CS 501', 'CS 513', 'CS 545']},
                  'SYEN': {'required': ['SYS 671', 'SYS 612', 'SYS 800'],
                           'electives': ['SSW 810', 'SSW 565', 'SSW 540']}}
        self.assertEqual(self.rep.info_major, expect)

    def test_info_student(self):
        expect = {'10103': {'name': 'Baldwin, C', 'dept': 'SFEN'},
                  '10115': {'name': 'Wyatt, X', 'dept': 'SFEN'},
                  '10172': {'name': 'Forbes, I', 'dept': 'SFEN'},
                  '10175': {'name': 'Erickson, D', 'dept': 'SFEN'},
                  '10183': {'name': 'Chapman, O', 'dept': 'SFEN'},
                  '11399': {'name': 'Cordova, I', 'dept': 'SYEN'},
                  '11461': {'name': 'Wright, U', 'dept': 'SYEN'},
                  '11658': {'name': 'Kelly, P', 'dept': 'SYEN'},
                  '11714': {'name': 'Morton, A', 'dept': 'SYEN'},
                  '11788': {'name': 'Fuller, E', 'dept': 'SYEN'}}
        self.assertEqual(self.rep.info_student, expect)

    def test_info_instructor(self):
        expect = {'98765': {'name': 'Einstein, A', 'dept': 'SFEN'},
                  '98764': {'name': 'Feynman, R', 'dept': 'SFEN'},
                  '98763': {'name': 'Newton, I', 'dept': 'SFEN'},
                  '98762': {'name': 'Hawking, S', 'dept': 'SYEN'},
                  '98761': {'name': 'Edison, A', 'dept': 'SYEN'},
                  '98760': {'name': 'Darwin, C', 'dept': 'SYEN'}}
        self.assertEqual(self.rep.info_instructor, expect)

    def test_info_grade(self):
        expect = [['10103', 'SSW 567', 'A', '98765'], ['10103', 'SSW 564', 'A-', '98764'],
                  ['10103', 'SSW 687', 'B', '98764'], ['10103', 'CS 501', 'B', '98764'],
                  ['10115', 'SSW 567', 'A', '98765'], ['10115', 'SSW 564', 'B+', '98764'],
                  ['10115', 'SSW 687', 'A', '98764'], ['10115', 'CS 545', 'A', '98764'],
                  ['10172', 'SSW 555', 'A', '98763'], ['10172', 'SSW 567', 'A-', '98765'],
                  ['10175', 'SSW 567', 'A', '98765'], ['10175', 'SSW 564', 'A', '98764'],
                  ['10175', 'SSW 687', 'B-', '98764'], ['10183', 'SSW 689', 'A', '98763'],
                  ['11399', 'SSW 540', 'B', '98765'], ['11461', 'SYS 800', 'A', '98760'],
                  ['11461', 'SYS 750', 'A-', '98760'], ['11461', 'SYS 611', 'A', '98760'],
                  ['11658', 'SSW 540', 'F', '98765'], ['11714', 'SYS 611', 'A', '98760'],
                  ['11714', 'SYS 645', 'C', '98760'], ['11788', 'SSW 540', 'A', '98765']]
        self.assertEqual(self.rep.info_grade, expect)





if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

