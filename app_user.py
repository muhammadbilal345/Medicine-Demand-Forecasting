from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask import session

app = Flask(__name__, static_folder='static')
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

def is_logged_in():
    return 'logged_in' in session and session['logged_in']

@app.route('/main')
def main():
    return render_template('main.html', is_landing_page=True)

@app.route('/',methods=['GET', 'POST'])
def ind():
    if not is_logged_in():
        return redirect(url_for('main'))  
    return render_template('index.html')

@app.route('/index',methods=['GET', 'POST'])
def index():
    if not is_logged_in():
        return redirect(url_for('main'))
    return render_template('index.html')

@app.route('/AboutUs',methods=['GET', 'POST'])
def aboutus():
    if not is_logged_in():
        return redirect(url_for('main'))
    return render_template('AboutUs.html')

@app.route("/ContactUs",methods=['GET', 'POST'])
def contactus():
    if not is_logged_in():
        return redirect(url_for('main'))
    return render_template('ContactUs.html')

@app.route('/learn',methods=['GET', 'POST'])
def learn():
    if not is_logged_in():
        return redirect(url_for('main'))
    return render_template('learn.html')

@app.route('/tutorial',methods=['GET', 'POST'])
def tutorial():
    if not is_logged_in():
        return redirect(url_for('main'))
    return render_template('tutorial.html')

@app.route('/service',methods=['GET', 'POST'])
def service():
    if not is_logged_in():
        return redirect(url_for('main'))
    
    return render_template('service.html')
@app.route('/dataset',methods=['GET', 'POST'])
def dataset():
    if not is_logged_in():
        return redirect(url_for('main'))
    return render_template('dataset.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('main'))

@app.route('/split', methods=['POST'])
def sign_in_split():
    if 'admin' in request.form:
        return redirect('adminsignin')
    else:
        return redirect('signin')
    
@app.route('/adminsignin', methods=['GET', 'POST'])
def adminsignin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM admin WHERE email=%s AND password=%s", (email, password))
        user = cur.fetchone()

        if user:
            session['logged_in'] = True
            return redirect('http://127.0.0.1:5002/')
        else:
            flash('Invalid email or password')

    return render_template('adminsignin.html', is_landing_page=True)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM students WHERE email=%s AND password=%s", (email, password))
        user = cur.fetchone()

        if user:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password')

    return render_template('signin.html', is_landing_page=True)

@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        mysql.connection.commit()
        flash("Account has been created Successfully")
        return redirect(url_for('signup'))
    return render_template('/signup.html', is_landing_page=True)

if __name__ == '__main__':
    app.run(debug=True)