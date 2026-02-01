from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    admission_progress = StringField('Admission Progress', validators=[DataRequired()])
    data_category = StringField('Data Category', validators=[DataRequired()])
    attendance = IntegerField('Attendance')
    submit = SubmitField('Submit')

class StaffForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    experience = StringField('Experience', validators=[DataRequired()])
    daily_tasks = StringField('Daily Tasks', validators=[DataRequired()])
    attendance = IntegerField('Attendance')
    submit = SubmitField('Submit')

class EnquiryForm(FlaskForm):
    student_name = StringField('Student Name', validators=[DataRequired()])
    course = StringField('Course', validators=[DataRequired()])
    mode_of_enquiry = SelectField('Mode of Enquiry', choices=[('Direct walk in', 'Direct walk in'), ('Telephone interview', 'Telephone interview')], validators=[DataRequired()])
    staff_assigned = StringField('Staff Assigned', validators=[DataRequired()])
    status = StringField('Status', validators=[DataRequired()])
    submit = SubmitField('Submit')
