from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app, db, bcrpyt
from flaskblog.models import User, Post



data = [
    {"name": "Ranjit","age": 22,"emp":'TCS', "address": "Abad"},
    {"name": "asmf","age": 32, "emp": "AWS","address": "Abad"},
    {"name": "dsasit","age": 12, "emp": "Google", "address": "Abad"}
    ]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = data)


@app.route("/about")
def about():
    return render_template('about.html', title = "About")


@app.route("/register", methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrpyt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for { form.username.data }!', category='success')
        return redirect(url_for('login'))
    
    elif not form.validate_on_submit():
        flash(f'Please Enter correct values', category='error')
        return render_template('register.html', title = 'register', form = form)
    
    return render_template('register.html', title = 'Register', form = form)


@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ranjitdav@gmail.com' and form.password.data == 'Ranjit':
            return redirect(url_for('home'))
        else:
            flash("Please enter valid credentials")
    return render_template('login.html', title = 'Login', form = form)

