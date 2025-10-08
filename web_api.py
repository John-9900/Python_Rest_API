from flask import Flask, request

import sqlite3

app = Flask(__name__)


@app.route("/register", methods=['POST'])
def register():
    try:
        data = request.get_json()
        connection = sqlite3.connect('sample10.db')
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS user_data(user_name text,password text)")
        cursor.execute("INSERT INTO user_data VALUES ('{}','{}')".format(data["user_name"], data["password"]))
        connection.commit()
        connection.close()
        return "User registeration has been done"
    except:
        return "Something happend wrong"


@app.route("/show")
def show():
    try:

        connection = sqlite3.connect("sample10.db")
        cursor = connection.cursor()
        df = list(cursor.execute("SELECT * FROM user_data"))
        return {"Facebook User Login Data": df}
    except:
        return "Something happend wrong"


@app.route("/update", methods=['POST'])
def update():
    try:
        data = request.get_json()
        connection = sqlite3.connect("sample10.db")
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE  user_data SET password= '{}' WHERE user_name= '{}'".format(data["password"], data["username"]))
        connection.commit()
        connection.close()
        return "User's password has been successfully updated"
    except:
        return "Something happend wrong"


@app.route("/delete", methods=['POST'])
def delete():
    try:
        data = request.get_json()
        connection = sqlite3.connect("sample10.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM user_data WHERE user_name= '{}'".format(data["username"]))
        connection.commit()
        connection.close()
        return "User data has been delete successfully"
    except:
        return "Something wrong happened"


app.run(port=1010)