"""
The framework to summarize student and instructor data.
"""
from collections import defaultdict
import os
from prettytable import PrettyTable


class Repository:
    """ Hold the students, instructors and grades for a single University. """

    def __init__(self, directory):
        """ initialize Repository"""
        self.directory = directory  # NOT mandatory!
        self.info_grade = list()
        self.info_person = defaultdict(lambda: dict())
        # self.files_summary = defaultdict(lambda: defaultdict(str))
        self.file_list = os.listdir(self.directory)

        self.analyze_files()  # summarize the python files data

    def analyze_files(self):
        """ populate the summarized data into self.files_summary """
        if not ["grades.txt", "instructors.txt", "students.txt"] <= self.file_list:
            raise FileNotFoundError("illegal input")

        os.chdir(self.directory)  # change current directory to "directory"
        for file in ["grades.txt", "instructors.txt", "students.txt"]:
            try:
                fp = open(file, 'r')
            except FileNotFoundError:
                raise FileNotFoundError(f"cannot open {file}")
            else:
                with fp:
                    if file == "grades.txt":
                        for line in fp:
                            list_line = line.rstrip().split()
                            # check if line is legal
                            if len(list_line) == 5 and len(list_line[0]) == 5 and list_line[0].startswith('1') and \
                                    len(list_line[-1]) == 5 and list_line[-1].startswith('9') and \
                                    list_line[0].isdigit() and list_line[2].isdigit() and list_line[-1].isdigit() and \
                                    list_line[1].isalpha() and list_line[-2] in ['A', 'A+', 'A-', 'B', 'B+', 'B-', 'C',
                                                                                 'C+', 'C-', 'D', 'D+', 'D-', 'F']:
                                # course = " ".join(list_line[1], list_line[2])
                                # self.files_summary[list_line[0]]["course_and_grade"] += (course+'='+list_line[-2]+',')
                                # self.files_summary[list_line[-1]]["course"] += (course + ',')
                                self.info_grade.append(list_line)
                            else:
                                raise ValueError(f"illegal input in {file}, the line is {line}")


                    else:  # file == "instructors.txt" or file == "students.txt"
                        for line in fp:
                            list_line = line.split(',')
                            # check if line is legal
                            if len(list_line) == 2:
                                cwid = list_line[0].split()[0]
                                name = list_line[0].split()[-1] + ',' + list_line[1][:2]
                                dept = list_line[1][2:].strip()

                                # check if attributes are legal
                                if len(cwid) == 5 and ((cwid.startswith('1') and file == "students.txt") or \
                                                       (cwid.startswith('9') and file == "instructors.txt")):
                                    self.info_person[cwid]["name"] = name
                                    self.info_person[cwid]["dept"] = dept
                                else:
                                    raise ValueError(f"illegal input in {file}, the line is {line}")
                            else:
                                raise ValueError(f"illegal input in {file}, the line is {line}")


class Student:
    """
    Hold all of the details of a student, including a defaultdict(str) to store the classes
    taken and the grade where the course is the key and the grade is the value.
    """

    def __init__(self, cwid, directory):
        self.cwid = cwid
        rep = Repository(directory)
        self.name = rep.info_person[self.cwid]["name"]
        self.dept = rep.info_person[self.cwid]["dept"]
        self.courses = list()
        for list_ in rep.info_grade:
            if self.cwid in list_:
                self.courses.append(list_[1] + ' ' + list_[2])
        self.courses = self.sort_courses(self.courses)

    def sort_courses(self, a_list):
        numbers = defaultdict(str)
        for course in a_list:
            numbers[int(course.split()[-1])] = course
        sorted_numbers = list(numbers.keys())
        sorted_numbers.sort()
        new_courses = list()
        for i in sorted_numbers:
            for j in numbers.keys():
                if i == j:
                    new_courses.append(numbers[j])

        return new_courses


class Instructor:
    """
    Hold all of the details of an instructor, including a defaultdict(int) to store
    the names of the courses taught along with the number of students
    """
    def __init__(self, cwid, directory):
        self.cwid = cwid
        rep = Repository(directory)
        self.name = rep.info_person[self.cwid]["name"]
        self.dept = rep.info_person[self.cwid]["dept"]
        self.course_student_dict = self.count_students(rep.info_grade)

    def count_students(self, a_list):
        course_students = defaultdict(int)
        for small_list in a_list:
            if self.cwid in small_list:
                course_name = small_list[1] + " " + small_list[2]
                course_students[course_name] += 1
        return course_students


def pretty_print(directory):
    """ pretty print students and instructors """
    rep = Repository(directory)
    pt_students = PrettyTable(field_names=["CWID", "Name", "Completed Courses"])
    pt_instructors = PrettyTable(field_names=["CWID", "Name", "Dept", "Course", "Students"])

    for cwid in rep.info_person.keys():
        if cwid.startswith('1'):
            s = Student(cwid, directory)
            pt_students.add_row([s.cwid, s.name, s.courses])

        if cwid.startswith('9'):
            ins = Instructor(cwid, directory)
            for course in ins.course_student_dict.keys():
                pt_instructors.add_row([ins.cwid, ins.name, ins.dept, course, ins.course_student_dict[course]])

    print("Student Summary")
    print(pt_students)
    print("Instructor Summary")
    print(pt_instructors)


def main():
    """ pretty print """
    path = os.path.dirname(os.path.abspath(__file__))
    pretty_print(path + "\\HW09")

    #  pretty_print("D:\\2019_Fall_Stevens\\ssw810\\homework\\HW09")
    """
    rep = Repository("D:\\2019_Fall_Stevens\\ssw810\\homework\\HW09")

    s = Student("10103", "D:\\2019_Fall_Stevens\\ssw810\\homework\\HW09")
    print(s.courses)
    t = Instructor("98764", "D:\\2019_Fall_Stevens\\ssw810\\homework\\HW09")
    print(t.course_student_dict)
    """


main()
