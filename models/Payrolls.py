from app import db


class PayrollsModel(db.Model):
    __tablename__ = 'payrolls'
    id = db.Column(db.Integer,primary  = True)
    overtime = db.Column(db.Float)
    month = db.Column(db.String(20),nullable = False)
    loan_deducted = db.Column(db.Float)
    advance_pay = db.Column(db.Float)
    gross_salary = db.Column(db.Float)
    personal_relief = db.Column(db.Float)
    taxable_amount = db.Column(db.Float)
    PAYE = db.Column(db.Float)
    NHIF = db.Column(db.Float)
    NSSF = db.Column(db.Float)
    net_salary =db.Column(db.Float)
    employee_id = db.Column(db.Integer,db.Foreignkey('employees.id'))

    # create
    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()


