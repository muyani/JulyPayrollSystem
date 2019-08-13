# importing flask class
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from config import Development,Testing
from resources.employees import Employee
import pygal





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
    departments = DepartmentModel.fetch_all()
    return render_template('employees.html',this_department = this_department,idara = departments)

@app.route('/payrolls/<int:emp_id>')
def payrolls(emp_id):
    employee = EmployeesModel.fetch_by_id(emp_id)
    return render_template('payrolls.html',employee = employee)

# registering a route
@app.route('/')
# function to run when clients visit this route
def home():
    departments = DepartmentModel.fetch_all()
    all_employees = EmployeesModel.fetch_all()
    male = 0
    female = 0
    others = 0
    for each in all_employees:
        if each.gender == 'm':
            male += 1
        elif each.gender == 'f':
            female +=1
        else:
            others +=1
    pie_chart = pygal.Pie()
    pie_chart.title = 'Comparing Company Employees by Gender'
    pie_chart.add('Male', male)
    pie_chart.add('Female', female)
    pie_chart.add('Others', others)
    graph = pie_chart.render_data_uri()

    line_chart = pygal.Bar()
    line_chart.title = 'Salary cost per Department'
    for each_dept in departments:
        line_chart.add(each_dept.name, DepartmentModel.fetch_total_payroll_by_id(each_dept.id) )
    bar_graph = line_chart.render_data_uri()


    # print(graph)
    # print(departments)
    # print(departments)
    return render_template('index.html',idara = departments,graph = graph,bar_graph = bar_graph)

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
    jina_ya_emp = request.form['name']
    kra_pin = request.form['kra_pin']
    gender = request.form['gender']
    national_id = request.form['national_id']
    email = request.form['email']
    department_id = int(request.form['department'])
    basic_salary = request.form['basic_salary']
    benefits = request.form['benefits']
    emp = EmployeesModel(full_name=jina_ya_emp,gender=gender,kra_pin=kra_pin,email=email,national_id=national_id,
                         department_id=department_id,basic_salary=basic_salary,benefits=benefits)
    emp.insert_to_db()
    return redirect(url_for('home'))

@app.route('/editEmployee/<int:id>',methods=['POST'])
def editEmployee(id):
    jina_ya_emp = request.form['name']
    kra_pin = request.form['kra_pin']
    gender = request.form['gender']
    national_id = request.form['national_id']
    email = request.form['email']
    department_id = int(request.form['department'])
    basic_salary = request.form['basic_salary']
    benefits = request.form['benefits']

    if gender == "na":
        gender = None
    if department_id == "0":
        department_id = None

    EmployeesModel.update_by_id(id=id,full_name=jina_ya_emp,gender=gender,
                                kra_pin=kra_pin,email=email,national_id=national_id,
                                department_id=department_id,basic_salary=basic_salary,
                                benefits=benefits)
    this_emp = EmployeesModel.fetch_by_id(id=id)
    this_dept = this_emp.department
    return redirect(url_for('employees',dept_id = this_dept.id))

@app.route('/deleteEmployee/<int:id>')
def deleteEmployee(id):
    this_emp = EmployeesModel.fetch_by_id(id=id)
    this_dept = this_emp.department
    EmployeesModel.delete_by_id(id)
    return redirect(url_for('employees',dept_id=this_dept.id))







# run flask
# if __name__ == '__main__':
#     app.run()
