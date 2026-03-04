from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root123'
app.config['MYSQL_DB'] = 'mydatabase'

mysql = MySQL(app)

@app.route("/")
def test():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT 1")
    return "Database Connected Successfully"
@app.route("/add")
def add():

    cursor = mysql.connection.cursor()

    cursor.execute(
        "INSERT INTO users(name,email,password) VALUES(%s,%s,%s)",
        ("Viresh","viresh@gmail.com","1234")
    )

    mysql.connection.commit()

    cursor.close()

    return "User added successfully"
if __name__ == "__main__":
    app.run(debug=True)