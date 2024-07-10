from flask import Flask, render_template,request,redirect
import sqlite3

app = Flask(__name__)

# Creating Routes  
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add_account',methods=["GET","POST"])
def add_account():

    if request.method == "POST": 

      # extract data from request
      anum = request.form.get('acnum')
      atype = request.form.get('actype')
      oname = request.form.get('owname')
      abranch = request.form.get('branch')
      gen = request.form.get('gender')
      bal = request.form.get('balance')

      
      #create connection with DB
      connection = sqlite3.connect("bank.db")
      cursor = connection.cursor()

      # store in database 
      cursor.execute("INSERT INTO user(acnum, actype, owname, branch, gender, balance) VALUES(?, ?, ?, ?, ?, ?)",
                      (anum,atype,oname,abranch,gen,bal))

      # Connection commit
      connection.commit()

      # Connection close
      cursor.close()
      connection.close()

      return redirect("/add_account")

    else:
      return render_template("add_account.html")

@app.route('/acc_update',methods=["POST","GET"])
def acc_update():
  if request.method == "POST":
        id = request.args.get('id')
        anum = request.form.get('acnum')
        atype = request.form.get('actype')
        oname = request.form.get('owname')
        abranch = request.form.get('branch')
        gen = request.form.get('gender')
        bal = request.form.get('balance')

        connection = sqlite3.connect("bank.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE user SET acnum = ?, actype = ?, owname = ?, branch = ?, gender = ?, balance = ? WHERE id = ?",
                       (anum, atype, oname, abranch, gen, bal, id))
        connection.commit()
        cursor.close()
        connection.close()

        return redirect("/table")
  else:
        id = request.args.get('id')
        connection = sqlite3.connect("bank.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user WHERE id = ?", (id,))
        account = cursor.fetchone()
        cursor.close()
        connection.close()

        return render_template("acc_update.html", account=account)

@app.route('/table')
def table():
     # Create connection with DB
    connection = sqlite3.connect("bank.db")
    cursor = connection.cursor()

    # Fetch all records from the user table
    cursor.execute("SELECT * FROM user")
    accounts = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    connection.close()

    return render_template("table.html", accounts=accounts)

@app.route('/delete')
def delete():
    # Extract the id
    serial_number = request.args.get('id')

    # Create connection with DB
    connection = sqlite3.connect("bank.db")
    cursor = connection.cursor()

    # Delete the record from the user table
    cursor.execute("DELETE FROM user WHERE id = ?", (serial_number,))

    # Commit the connection
    connection.commit()

    # Close cursor and connection
    cursor.close()
    connection.close()

    return redirect("/table")

if __name__ == "__main__":
    app.run() 