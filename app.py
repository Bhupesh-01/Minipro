from flask import Flask, request, render_template, redirect, url_for
import mysql.connector as c

app = Flask(__name__)

def connect_to_db():
    return c.connect(host="localhost", user="root", password="Pawara@123", database="miniproject")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/insert', methods=['POST'])
def insert_data():
    name = request.form['name']
    rollno = request.form['rollno']
    student_class = request.form['class']
    con = connect_to_db()
    cursor = con.cursor()
    query = "INSERT INTO student_details VALUES (%s, %s, %s)"
    cursor.execute(query, (name, rollno, student_class))
    con.commit()
    con.close()
    return redirect(url_for('home'))

@app.route('/update', methods=['POST'])
def update_data():
    name = request.form['name']
    rollno = request.form['rollno']
    con = connect_to_db()
    cursor = con.cursor()
    query = "UPDATE student_details SET name = %s WHERE rollno = %s"
    cursor.execute(query, (name, rollno))
    con.commit()
    con.close()
    return redirect(url_for('home'))

@app.route('/delete', methods=['POST'])
def delete_data():
    rollno = request.form['rollno']
    con = connect_to_db()
    cursor = con.cursor()
    query = "DELETE FROM student_details WHERE rollno = %s"
    cursor.execute(query, (rollno,))
    con.commit()
    con.close()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
