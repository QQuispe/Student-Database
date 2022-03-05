from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
db = 'students.db'

@app.route('/')
@app.route('/home')
def home_page():
    student_data = query_studentdb()
    return render_template('home.html', student_data=student_data)

# route for create page
@app.route('/create', methods = ['GET', 'POST'])
def create_student():
    if request.method == 'GET':
        return render_template('create.html')
    else:
        new_student = (
            request.form['id'],
            request.form['name'],
            request.form['points'],
        )
        create_studentdb(new_student)
        student_data = query_studentdb()
        return render_template('home.html', student_data=student_data)

# route for update page
@app.route('/update', methods = ['GET', 'POST'])
def update_student():
    if request.method == 'GET':
        return render_template('update.html')
    else:
        current_student = (
            request.form['id'],
            request.form['name'],
            request.form['points'],
        )
        update_studentdb(current_student)
        student_data = query_studentdb()
        return render_template('home.html', student_data=student_data)

# route for delete page
@app.route('/delete', methods = ['GET', 'POST'])
def delete_student():
    if request.method == 'GET':
        return render_template('delete.html')
    else:
        current_student = (
            request.form['id'],
        )
        delete_studentdb(current_student)
        student_data = query_studentdb()
        return render_template('home.html', student_data=student_data)

# function that pulls all data from database
def query_studentdb():
    con = sqlite3.connect(db)
    c = con.cursor()
    c.execute("""
    SELECT * FROM student_info
    """)
    info = c.fetchall()
    return info

#function to create a student in the database
def create_studentdb(new_student):
    con = sqlite3.connect(db)
    c = con.cursor()
    cquery = 'INSERT INTO student_info (id, name, points) VALUES (?,?,?)'
    c.execute(cquery, new_student)
    con.commit()
    con.close()

# function to update a student in the database
def update_studentdb(current_student):
    con = sqlite3.connect(db)
    c = con.cursor()
    cquery = """Update student_info set name = ?, points = ? where id = ?"""
    col = current_student[1], current_student[2], current_student[0]
    c.execute(cquery, col)
    con.commit()
    con.close()


# function to delete a student in the database
def delete_studentdb(current_student):
    con = sqlite3.connect(db)
    c = con.cursor()
    cquery = """Delete from student_info where id = ?"""
    c.execute(cquery, current_student)
    con.commit()
    con.close()

if __name__ == '__main__':
    app.run()