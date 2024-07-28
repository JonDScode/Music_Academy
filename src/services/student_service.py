from src.models.models import Student
from sqlalchemy.exc import SQLAlchemyError

def get_student(db_session, student_id: int):
    try:
        return db_session.query(Student).filter(Student.id == student_id).first()
    except SQLAlchemyError as e:
        print(f"Error fetching student: {e}")
        return None

def get_all_students(db_session):
    try:
        return db_session.query(Student).all()
    except SQLAlchemyError as e:
        print(f"Error fetching all students: {e}")
        return []

def create_student(db_session, student_data: dict):
    try:
        new_student = Student(**student_data)
        db_session.add(new_student)
        db_session.commit()
        return new_student
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Error creating student: {e}")
        return None

def update_student(db_session, student_id: int, update_data: dict):
    try:
        student = db_session.query(Student).filter(Student.id == student_id).first()
        if student is None:
            return None
        for key, value in update_data.items():
            setattr(student, key, value)
        db_session.commit()
        return student
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Error updating student: {e}")
        return None

def delete_student(db_session, student_id: int):
    try:
        student = db_session.query(Student).filter(Student.id == student_id).first()
        if student is None:
            return None
        db_session.delete(student)
        db_session.commit()
        return student
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Error deleting student: {e}")
        return None
