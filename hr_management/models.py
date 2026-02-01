from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    admission_progress = db.Column(db.String(100), nullable=False)
    data_category = db.Column(db.String(100), nullable=False)
    attendance = db.Column(db.Integer, default=0)

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    experience = db.Column(db.String(200), nullable=False)
    daily_tasks = db.Column(db.String(200), nullable=False)
    attendance = db.Column(db.Integer, default=0)

class Enquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    mode_of_enquiry = db.Column(db.String(50), nullable=False)
    staff_assigned = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
