"""
Build a new web page to display a summary of each Instructor with her CWID, Name, Department,
Course, and the number of students in the course.
"""

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/instructor_courses')
def instructor_courses():
    """
    Build a new web page to display a summary of each Instructor with her CWID, Name, Department,
    Course, and the number of students in the course.
    """
    dbpath = "D:\\2019_Fall_Stevens\\ssw810\\homework\\HW12\\810_startup.db"
    try:
        db = sqlite3.connect(dbpath)
    except sqlite3.OperationalError:
        return f"Error: Unable to open database at {dbpath}"
    else:
        query = "select CWID, Instructor, Dept, Course, count(*) as Students " \
                "from instructors join grades on CWID=InstructorCWID group by Course"

        data = [{'cwid': cwid, 'name': name, 'dep': dep, 'course': course, 'students': students}
                for cwid, name, dep, course, students in db.execute(query)]

        db.close()

        return render_template('instructor_courses.html',
                               title="Stevens Repository",
                               table_title="Number of students by course and instructor",
                               instructors=data)


app.run(debug=True)
