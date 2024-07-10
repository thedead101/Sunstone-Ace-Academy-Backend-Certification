from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#connect the flask app(server) with sqllite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'

#create object of SQLAlchemy
database = SQLAlchemy(app)

# Create class of table

class Student(database.Model):
    id = database.Column(database.Integer, primary_key= True, autoincrement=True)
    name = database.Column(database.String(100), nullable= False)
    age = database.Column(database.Integer, nullable= False)
    gender = database.Column(database.String(10), nullable= False)
    grade = database.Column(database.String(10), nullable= False)
    email = database.Column(database.String(200), nullable= False)


@app.route('/')
def index():
    return render_template("index1.html")

@app.route('/table')
def table():
        # fetch all the tasks from the database
        alldetails = Student.query.all()
 
        # returning the response
        return render_template("table.html",alldetails=alldetails)
    # return render_template("table.html")

@app.route('/add_details',methods=["POST","GET"])
def add_details():

     if request.method == "POST":
        
        # fetch the values 
        stname = request.form.get('name')
        sage = request.form.get('age')
        sgender = request.form.get('gender')
        sgrade = request.form.get('grade')
        semail = request.form.get('email')

        # add to database
        student_det = Student(name=stname,age=sage,gender=sgender,grade=sgrade,email=semail)
        database.session.add(student_det)
        database.session.commit()

         # returning the response
        return redirect("/add_details")
     else:
        return render_template("add_details.html")

@app.route('/updatedetails',methods=["POST","GET"])
def update():

   serial_number = request.args.get('id')
   reqstu = Student.query.filter_by(id= serial_number).first()

   if request.method == 'POST':
      
      # Update the title 
      updatedname = request.form.get('name')
      updatedage = request.form.get('age')
      updatedgender = request.form.get('gender')
      updatedgrade = request.form.get('grade')
      updatedemail = request.form.get('email')

      # changing the value of existing task
      reqstu.name = updatedname
      reqstu.age = updatedage
      reqstu.gender = updatedgender
      reqstu.grade = updatedgrade
      reqstu.email = updatedemail

      # committing changes to database
      database.session.add(reqstu)
      database.session.commit()

      return redirect("/table")
   else:
      return render_template("updatedetails.html",reqstu = reqstu)

@app.route('/delete')
def delete():
    # extract the sno
   serial_number = request.args.get('id')

   # extract the sno
   student = Student.query.filter_by(id=serial_number).first()
  #  print(task)

   database.session.delete(student)
   database.session.commit()

   return redirect("/table")

if __name__ == "__main__":
  redirect("index1.html")
#let's run the flask application
  app.run()