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
    # Read
    @classmethod
    def fetch_by_id(cls,id):
        return cls.query.filter_by(id = id).first()

    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    # Update
    @classmethod
        # read on keyword/default functions
    def update_by_id(cls,id,full_name = None,gender = None,kra_pin = None,email = None,national_id = None,
                     department_id = None,basic_salary = None,benefits = None):
        record = cls.fetch_by_id(id=id)
        if full_name:
            record.full_name = full_name
        if gender:
            record.gender = gender
        if kra_pin:
            record.kra_pin = kra_pin
        if email:
            record.email = email
        if national_id:
            record.national_id = national_id
        if department_id:
            record.department_id = department_id
        if basic_salary:
            record.basic_salary = basic_salary
        if benefits:
            record.benefits = benefits
        db.session.commit()
        return True

        # delete
    @classmethod
    def delete_by_id(cls,id):
        record = cls.query.filter_by(id=id)
        record.delete()
        db.session.commit()
        return True

