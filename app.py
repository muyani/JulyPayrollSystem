# importing flask class
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from config import Development,Testing


# instantiating class flask
app = Flask(__name__)
# this is a config parameter that shows where our database lives
app.config.from_object(Development)
# app.config.from_object(Testing)
db = SQLAlchemy(app)
from models.Employees import EmployeesModel
from models.Departments import DepartmentModel


# this decorator will tell flask to run this function before any other route
@app.before_first_request
def create_tables():
    db.create_all()

# registering a route
@app.route('/')
# function to run when clients visit this route
def hello_world():
    return render_template('index.html')

@app.route('/name')
def name():
    return "Muyani Letina"


# run flask
# if __name__ == '__main__':
#     app.run()
