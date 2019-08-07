# importing flask class
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from config import Development,Testing
from resources.employees import Employee





# instantiating class flask
app = Flask(__name__)
# this is a config parameter that shows where our database lives
app.config.from_object(Development)
# app.config.from_object(Testing)
db = SQLAlchemy(app)
from models.Employees import EmployeesModel
from models.Departments import DepartmentModel


# this decorator will tell flask to run this function before any other route
# TODO:read about flask-migrate
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/employees/<int:dept_id>')
def employees(dept_id):
    this_department = DepartmentModel.fetch_by_id(dept_id)
    employees = this_department.employees
    return render_template('employees.html',this_department = this_department)

@app.route('/payrolls/<int:emp_id>')
def payrolls(emp_id):
    employee = EmployeesModel.fetch_by_id(emp_id)
    return render_template('payrolls.html',employee = employee)

# registering a route
@app.route('/')
# function to run when clients visit this route
def home():
    departments = DepartmentModel.fetch_all()
    print(departments)
    return render_template('index.html',idara = departments)

@app.route('/generate_payroll/<int:id>',methods = ['POST'])
def generate_payroll(id):
    this_employee = EmployeesModel.fetch_by_id(id)
    payroll = Employee(this_employee.full_name,this_employee.basic_salary,this_employee.benefits)
    nhif = payroll.nhif
    print("NSSF",payroll.nssf)
    print("PAYE",payroll.payeTax)
    print("NET",payroll.netSalary)
    print("Gross",payroll.grossSalary)
    print("Personal Relief",payroll.personal_relief)
    print("Taxable amount",payroll.chargeable_pay)



@app.route('/newDepartment',methods=['POST'])
def newDepartment():
    department_name = request.form['department']
    if DepartmentModel.fetch_by_name(department_name):
        # read more on bootsrap alerts with flash
        flash("Department" + department_name + "already exist")
        return redirect(url_for('home'))
    department = DepartmentModel(name= department_name)
    department.insert_to_db()
    return redirect(url_for('home'))


@app.route('/newEmployee',methods=['POST'])
def newEmployee():
    name_of_employee = request.form['name']
    kra_pin = request.form['kra_pin']
    gender = request.form['gender']
    national_id = request.form['national_id']
    email = request.form['email']
    department_id = int(request.form['department'])
    basic_salary = request.form['basic_salary']
    benefits = request.form['benefits']
    emp = EmployeesModel(full_name=name_of_employee,gender=gender,kra_pin=kra_pin,email=email,national_id=national_id,
                         department_id=department_id,basic_salary=basic_salary,benefits=benefits)
    emp.insert_to_db()
    return redirect(url_for('home'))



# run flask
# if __name__ == '__main__':
#     app.run()
