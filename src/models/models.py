from src.db.database import db

class Student(db.Model):
    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    age = db.Column(db.Integer)
    telephone = db.Column(db.Integer)
    email = db.Column(db.String(255))
    is_assoc = db.Column(db.Boolean)
    fam_assoc_st_id = db.Column(db.Integer, db.ForeignKey("fam_assoc_st.id"))

    fam_assoc = db.relationship("FamAssocSt", back_populates="students")
    enrollments = db.relationship("Enrollment", back_populates="student")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age,
            "telephone": self.telephone,
            "email": self.email,
            "is_assoc": self.is_assoc,
            "fam_assoc_st_id": self.fam_assoc_st_id
        }


class FamAssocSt(db.Model):
    __tablename__ = "fam_assoc_st"

    id = db.Column(db.Integer, primary_key=True, index=True)
    assoc_student = db.Column(db.Integer)

    students = db.relationship("Student", back_populates="fam_assoc")

    def to_dict(self):
        return {
            "id": self.id,
            "assoc_student": self.assoc_student
        }


class NumClasses(db.Model):
    __tablename__ = "num_classes"

    id = db.Column(db.Integer, primary_key=True, index=True)
    num_classes = db.Column(db.Integer)
    dosccount_per = db.Column(db.Float)

    classes = db.relationship("Class", back_populates="num_classes")

    def to_dict(self):
        return {
            "id": self.id,
            "num_classes": self.num_classes,
            "dosccount_per": self.dosccount_per
        }


class Class(db.Model):
    __tablename__ = "class"

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(255))
    level_id = db.Column(db.Integer, db.ForeignKey("level.id"))
    price = db.Column(db.Float)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.teacher_id"))
    num_classes_id = db.Column(db.Integer, db.ForeignKey("num_classes.id"))

    teacher = db.relationship("Teacher", back_populates="classes")
    num_classes = db.relationship("NumClasses", back_populates="classes")
    level = db.relationship("Level", back_populates="classes")
    enrollments = db.relationship("Enrollment", back_populates="class_")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "level_id": self.level_id,
            "price": self.price,
            "teacher_id": self.teacher_id,
            "num_classes_id": self.num_classes_id
        }


class Teacher(db.Model):
    __tablename__ = "teacher"

    teacher_id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(255))
    lastname = db.Column(db.String(255))

    classes = db.relationship("Class", back_populates="teacher")

    def to_dict(self):
        return {
            "teacher_id": self.teacher_id,
            "name": self.name,
            "lastname": self.lastname
        }


class Level(db.Model):
    __tablename__ = "level"

    id = db.Column(db.Integer, primary_key=True, index=True)
    level_type = db.Column(db.String(255))

    classes = db.relationship("Class", back_populates="level")

    def to_dict(self):
        return {
            "id": self.id,
            "level_type": self.level_type
        }


class Enrollment(db.Model):
    __tablename__ = "enrollments"

    enrollment_id = db.Column(db.Integer, primary_key=True, index=True)
    class_id = db.Column(db.Integer, db.ForeignKey("class.id"))
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.teacher_id"))
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    student = db.relationship("Student", back_populates="enrollments")
    class_ = db.relationship("Class", back_populates="enrollments")
    teacher = db.relationship("Teacher")

    def to_dict(self):
        return {
            "enrollment_id": self.enrollment_id,
            "class_id": self.class_id,
            "teacher_id": self.teacher_id,
            "student_id": self.student_id,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
