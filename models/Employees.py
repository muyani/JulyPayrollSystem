from app import db

class EmployeesModel(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer,primary_key=True)
    full_name = db.Column(db.String(50),nullable=False)
    gender = db.Column(db.String(10),nullable=False)
    kra_pin = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(50),unique=True,nullable=False)
    national_id = db.Column(db.String(50),unique=True,nullable=False)
    department_id = db.Column(db.Integer,db.ForeignKey('departments.id'))
    basic_salary = db.Column(db.Float)
    benefits = db.Column(db.Float)

    # create
    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_by_id(cls,id):
        return cls.query.filter_by(id = id).first()


