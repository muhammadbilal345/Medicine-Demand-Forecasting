from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

@app.route('/userviewonly')
def userviewonly():
    cur1 = mysql.connection.cursor()
    cur1.execute("SELECT  * FROM students")
    user_data = cur1.fetchall()
    cur1.close()
    return render_template('userviewonly.html', return_user_data=user_data)

@app.route('/useredit')
def useredit():
    cur1 = mysql.connection.cursor()
    cur1.execute("SELECT  * FROM students")
    user_data = cur1.fetchall()
    cur1.close()
    return render_template('useredit.html', return_user_data=user_data)

@app.route('/adminrecordview')
def adminrecordview():
    cur2 = mysql.connection.cursor()
    cur2.execute("SELECT  * FROM admin")
    admin_data = cur2.fetchall()
    cur2.close()
    return render_template('adminrecordview.html', return_user_data=admin_data)

@app.route('/')
def Index():
    cur1 = mysql.connection.cursor()
    cur1.execute("SELECT  * FROM students")
    user_data = cur1.fetchall()
    cur1.close()

    cur2 = mysql.connection.cursor()
    cur2.execute("SELECT  * FROM admin")
    admin_data = cur2.fetchall()
    cur2.close()
    return render_template('index2.html', return_user_data=user_data, user_data_len=len(user_data), admin_data_len=len(admin_data) )


@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('useredit'))


@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE students
               SET name=%s, email=%s, password=%s
               WHERE id=%s
            """, (name, email, password, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True, port=5002)
