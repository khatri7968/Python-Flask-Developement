from flask import render_template, url_for, redirect, flash
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegristrationForm, LogInForm




from flaskblog.models import User, Post

posts = [
    {
        'author': 'Programming with Marsh',
        'title': 'Blog Post-1',
        'content': 'First Post content',
        'date_posted': 'May 21, 2019'
    },

    {
        'author': 'Corey Achafer',
        'title': 'Blog Post-2',
        'content': '2nd Post content',
        'date_posted': 'May 22, 2019'
    },

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('About.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegristrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data =="12345":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash("Login Uncsuccessful. Please check username and password", 'danger')
    return render_template('login.html', title='login', form=form)