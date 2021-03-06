import mysql.connector
import os
import logging
from logger import log
from flask import Flask, request, jsonify, redirect, render_template, url_for


logging.basicConfig(filename="LOG_flask.log",
                    filemode="a",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    datefmt='[%Y-%m-%d %H:%M:%S]')



app = Flask(__name__)

@log
def createConnection():
    c = mysql.connector.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_ROOT_PASSWORD'],
            auth_plugin=os.environ['MYSQL_AUTH_PLUGIN'],
            database=os.environ['MYSQL_DATABASE']
    )
    return c


@app.route("/")
@log
def home():
    return "home"


@app.route('/api', methods=['POST', 'GET'])
@log
def index():
    if request.method == 'POST':
       dest = request.form['destination']
       d1 = request.form['date_begin']
       d2 = request.form['date_end']
       y = request.form['year']
       if not dest:
           return redirect(url_for('searching_dates', d1=d1, d2=d2))

        elif not d1 and not d2:
            return redirect(url_for('searching-dest', dest=dest))

    else:
        return render_template('api.html')

        
@app.route('/searching-dest/<dest>', methods=['POST', 'GET'])
@log
def search_dest(dest):
    c = createConnection()
    cur = c.cursor()
    cur.execute('use vintage_ride')
    cur.execute("SELECT * FROM vintage_ride WHERE destination LIKE %s;", (dest))
    results = cur.fetchall()
    return render_template("results.html", results=results)
    if request.method == 'POST':
        mail = request.form["mail"]
        if not mail:
            return redirect(url_for('searching-dest', dest=dest))
        else:
            mailing()
            return render_template('api.html')




@app.route('/searching-dates/<d1>/<d2>/<y>', methods=['POST', 'GET'])
@log
def search_dates(d1, d2, y):
    c = createConnection()
    cur = c.cursor()
    cur.execute('use vintage_ride')
    cur.execute("SELECT * FROM vintage_ride WHERE departure_date<=%s AND end_date>=%s AND year LIKE %s;", (d1, d2, y))
    results = cur.fetchall()
    return render_template("results.html", results=results)
    if request.method == 'POST':
        mail = request.form["mail"]
        if not mail:
            return redirect(url_for('searching-dates', d1=d1, d2=d2, y=y))
        else:
            mailing()
            return render_template('api.html')





# def get_data():
#     c = mysql.connection.cursor()
#     c.execute('use vintage_ride')
#     c.execute('''select * from vintage_ride''')
#     data = c.fetchall()
#     return render_template("qzoriejuf.html", data=data")
#     # vintage_ride = []
#     # content = {}
#     # for result in data:
#     #     content = {'ID': result['ID'], 'title': result['title'], 'destination': result['destination'], 'departure_date': result['departure_date'], 'end_date': result['end_date'], 'year': result['year'], 'level': result['level']}
#     #     vintage_ride.append(content)
#     #     content = {}
#     mysql.connection.commit()
#     c.close()
    
#     return jsonify(data)





#Emailing:

import smtplib, ssl
import threading
@log
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
    server.quit()

if __name__=='__main__':
    app.run(host="0.0.0.0", port=4000, debug = True)