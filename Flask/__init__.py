import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, request, render_template, jsonify
from flask_mysqldb import MySQL
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)

app.config['MYSQL_HOST']='ms'
app.config['MYSQL_USER'] = 'app1'
app.config['MYSQL_PASSWORD'] = 'pwd'
app.config['MYSQL_DB'] = 'vintage_ride'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_PORT'] = '3306'

mysql = MySQL(app)

def log(func):
    def wrapper(*args, **kwargs):
        func_str = func.__name__
        args_str = '\t '.join(args)
        with open('LOG_init_flask.log', 'w') as f:
            f.write(func_str)
            f.write(args_str)
        return func(*args, **kwargs)
    return wrapper


@log
@app.route('/')
def get_data():
    c = mysql.connection.cursor()
    c.execute('''select * from vintage_ride''')
    data = c.fetchall()
    # vintage_ride = []
    # content = {}
    # for result in data:
    #     content = {'ID': result['ID'], 'title': result['title'], 'destination': result['destination'], 'departure_date': result['departure_date'], 'end_date': result['end_date'], 'year': result['year'], 'level': result['level']}
    #     vintage_ride.append(content)
    #     content = {}
    mysql.connection.commit()
    c.close()
    
    return jsonify(data)

#Emailing:

import smtplib

def mailing():
    sender_mail = "test@gmail.com"
    dest_mail = "merelle@gmail.com"
    password = input(str("Enter your mail password: "))
    message = "we have a match !! "

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_mail, password)
    print("logging sender_mail success")
    server.sendmail(sender_mail, dest_mail, message)
    print("mail has been send to ", dest_mail)

if __name__=='__main__':
    app.run(host="0.0.0.0", port=3002, debug = True)