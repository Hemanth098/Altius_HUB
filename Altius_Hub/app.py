from flask import render_template,Flask,redirect,session,url_for,flash,request
import sqlite3
from wtforms import StringField,PasswordField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,ValidationError
import bcrypt

def get_conn():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
class SignInForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = 'abcdefghi'
@app.route('/',methods=['GET','POST'])
def main():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print(username,password)
        passw = password
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT username,password FROM user WHERE username=? and password=?", (username,password))
        user = cursor.fetchone()
        print(user['password'])
        if not user:
            raise ValidationError("Username Already Present")
        if user['password']!= passw:
            raise ValidationError('Password Wrong')
        session['username'] = username
        return redirect(url_for('home'))
    return render_template('index.html',form=form)
@app.route('/SignIn',methods=['GET','POST'])
def SignIn():
    form = SignInForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print(username,password)
        passw = password
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM user WHERE username=?", (username,))
        if cursor.fetchone():
            raise ValidationError("Username Already Present")
        cursor.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, passw))
        conn.commit()
        conn.close()
        return redirect(url_for('main'))
    return render_template('SignIN.html',form=form)

@app.route('/home',methods = ['GET','POST'])
def home():
    if 'username' in session:
        return render_template('home.html')
    flash('Login First!!!')
    return redirect('SignIn')


with get_conn() as conn:
    conn.execute('''
                CREATE TABLE IF NOT EXISTS user (
                    Username TEXT NOT NULL PRIMARY KEY,
                    Password TEXT NOT NULL
                )
            ''')
    conn.execute('''
                CREATE TABLE IF NOT EXISTS book (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Book_Name TEXT NOT NULL,
                    YEAR_PUBLISHED INTEGER,
                    AUTHOR_NAME TEXT NOT NULL
                )
            ''')
    conn.execute('''
                CREATE TABLE IF NOT EXISTS product (
                    Username TEXT NOT NULL PRIMARY KEY,
                    Password TEXT NOT NULL
                )
            ''')
app.run(port='5050',debug='True')