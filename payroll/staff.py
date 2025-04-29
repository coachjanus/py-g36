from flask import Blueprint, render_template, url_for, current_app, request, redirect, flash
from payroll.database import get_db

bp = Blueprint('staff', __name__)



@bp.route("/staff/index")
def index():
    db = get_db()
    employees = db.execute('SELECT emp.id emp_id, employee_name, department_id, d.department_name, join_data, role_id, r.role_name FROM employee emp JOIN roles r ON emp.role_id = r.id JOIN department d ON department_id = d.id'
    ).fetchall()
    return render_template("staff/index.html", employees = employees)

@bp.route("/staff/create", methods=("GET", "POST"))
def create():
    db = get_db()
    departments = db.execute('SELECT * FROM department').fetchall()
    roles = db.execute('SELECT * FROM roles').fetchall()
    if request.method == "POST":
        employee_name = request.form['employee_name']
        department_id = int(request.form['department_id'])
        role_id = int(request.form['role_id'])
        weekly_solary = float(request.form['weekly_solary']) or 0
        commission_per_sale =float(request.form['commission_per_sale']) or 0
        hour_rate =float(request.form['hour_rate']) or 0
        
        db.execute("INSERT INTO employee (employee_name, department_id, role_id, weekly_solary, commission_per_sale, hour_rate) VALUES (?, ?, ?, ?, ?, ?)", (employee_name, department_id, role_id, weekly_solary, commission_per_sale, hour_rate))
        db.commit()
        
    else:
        return render_template("staff/create.html", roles = roles, departments=departments)
