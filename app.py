from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('me.html')

@app.route('/dane' , methods=['GET', 'POST'])
def dane():
   if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")