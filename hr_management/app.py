from flask import Flask, render_template, redirect, url_for
from config import Config
from models import db, Student, Staff, Enquiry
from forms import StudentForm, StaffForm, EnquiryForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students', methods=['GET', 'POST'])
def students():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(name=form.name.data, admission_progress=form.admission_progress.data,
                          data_category=form.data_category.data, attendance=form.attendance.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('students'))
    students = Student.query.all()
    return render_template('students.html', form=form, students=students)

@app.route('/staff', methods=['GET', 'POST'])
def staff():
    form = StaffForm()
    if form.validate_on_submit():
        staff = Staff(name=form.name.data, experience=form.experience.data,
                      daily_tasks=form.daily_tasks.data, attendance=form.attendance.data)
        db.session.add(staff)
        db.session.commit()
        return redirect(url_for('staff'))
    staff_members = Staff.query.all()
    return render_template('staff.html', form=form, staff=staff_members)

@app.route('/enquiries', methods=['GET', 'POST'])
def enquiries():
    form = EnquiryForm()
    if form.validate_on_submit():
        enquiry = Enquiry(student_name=form.student_name.data, course=form.course.data,
                          mode_of_enquiry=form.mode_of_enquiry.data, staff_assigned=form.staff_assigned.data,
                          status=form.status.data)
        db.session.add(enquiry)
        db.session.commit()
        return redirect(url_for('enquiries'))
    enquiries = Enquiry.query.all()
    return render_template('enquiries.html', form=form, enquiries=enquiries)

if __name__ == '__main__':
    app.run(debug=True)
