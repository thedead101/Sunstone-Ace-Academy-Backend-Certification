from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#connect the flask app(server) with sqllite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.db'

#create object of SQLAlchemy
database = SQLAlchemy(app)

# Create class of table
class Book(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(100), nullable=False)
    author = database.Column(database.String(100), nullable=False)
    year_published = database.Column(database.Integer, nullable=False)
    isbn = database.Column(database.String(13), unique=True, nullable=False)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/table')
def table():
        # fetch all the books from the database
        allbook = Book.query.all()
        # returning the response
        return render_template("table.html",allbook=allbook)

@app.route('/add_book',methods=["POST","GET"])
def add_book():

     if request.method == "POST":
        # fetch the values 
        bkname = request.form.get('title')
        bauname = request.form.get('author')
        byrpub = request.form.get('year_published')
        bisbn = request.form.get('isbn')

        # add to database
        book_det = Book(title=bkname,author=bauname,year_published=byrpub,isbn=bisbn)
        database.session.add(book_det)
        database.session.commit()

         # returning the response
        return redirect("/add_book")
     else:
        return render_template("add_book.html")

@app.route('/updatebook',methods=["POST","GET"])
def update():

   serial_number = request.args.get('id')
   reqbook = Book.query.filter_by(id= serial_number).first()

   if request.method == 'POST':
      
      # Update the title 
      updatedbname = request.form.get('title')
      updatedauthor = request.form.get('author')
      updatedyrpub = request.form.get('year_published')
      updatedisbn = request.form.get('isbn')

      # changing the value of existing task
      reqbook.title = updatedbname
      reqbook.author = updatedauthor
      reqbook.year_published = updatedyrpub
      reqbook.isbn = updatedisbn

      # committing changes to database
      database.session.add(reqbook)
      database.session.commit()

      return redirect("/table")
   else:
      return render_template("updatebook.html",reqbook = reqbook)

@app.route('/delete')
def delete():
    # extract the id
   serial_number = request.args.get('id')

   # extract the id
   book = Book.query.filter_by(id=serial_number).first()

   database.session.delete(book)
   database.session.commit()

   return redirect("/table")

if __name__ == "__main__":
  redirect("index.html")
#let's run the flask application
  app.run(debug=True)