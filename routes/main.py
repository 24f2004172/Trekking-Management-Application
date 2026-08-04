from flask import Blueprint, render_template, redirect, url_for
from models.user import User
from flask import request


main = Blueprint('main', __name__)

@main.route("/")
def index():
    args = request.args.to_dict()
    if args:
        if 'trekker' in args:
            return redirect(url_for('main.trekker'))
        elif 'admin' in args:
            return redirect(url_for('main.admin'))

    return render_template('index.html')

@main.route("/register")
def register():
    return render_template('register.html')

@main.route("/login")
def login():
    return render_template('login.html')

@main.route("/trekker")
def trekker():
    user_trek = User.query.get(0)
    template_trekker = f'''
            <h1> Hello {user_trek.name}, Nice to meet you! </h1>
            <h3> I got your email: {user_trek.email} </h3>
            <h3> Your password is {user_trek.password[0:4]}***** </h3>
        '''
    return template_trekker

@main.route("/admin")
def admin():
    user_admin = User.query.get(1)
    template_admin = f'''
                <h1> Hello {user_admin.name}, Nice to meet you! </h1>
                <h3> I got your email: {user_admin.email} </h3>
                <h3> Your password is {user_admin.password[0:4]}***** </h3>
                <h3> You have a previlage of Admin! </h3>
            '''
    return template_admin