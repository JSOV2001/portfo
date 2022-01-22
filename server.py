from ast import Return
from flask import Flask, render_template, request, redirect
import csv

#Se crea el servidor
app = Flask(__name__)

@app.route('/') #Cada vez que se accede a la dirección, haga lo de esta función
def my_home():
    return render_template("index.html")

@app.route('/about.html') 
def about():
    return render_template('about.html')

@app.route('/contact.html') 
def contact():
    return render_template('contact.html')

@app.route('/index.html') 
def index():
    return render_template('index.html')

@app.route('/work.html') 
def work():
    return render_template('work.html')

@app.route('/works.html') 
def works():
    return render_template('works.html')

@app.route('/thankyou.html') 
def thank_you():
    return render_template('thankyou.html')

"""
@app.route('/<string:page_name>') 
def html_page(page_name):
    return render_template(page_name)
"""
    
def write_to_file(data_dict):
    email = data_dict["email"]
    subject = data_dict["subject"]
    message = data_dict["message"]
    
    with open('database.txt', mode="a") as database_file: 
        database_file.write(f'\nEmail: {email}, Subject: {subject}, Message: {message}')

def write_to_csv(data_dict):
    with open('database.csv', newline='', mode="a") as database_file2:
        email = data_dict["email"]
        subject = data_dict["subject"]
        message = data_dict["message"]
        
        csv_writer = csv.writer(database_file2, delimiter=",", quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
#POST significa que el navegador quiere que le enviemos información
#GET significa que el navegador quiere que guardemos información
def submit_form():
    if request.method == "POST":
        try:
            data_of_the_form = request.form.to_dict()
            print(data_of_the_form)
            write_to_csv(data_of_the_form)
            write_to_file(data_of_the_form)
            return redirect("/thankyou.html")
        except:
            return "Did no save to database"
    else:
        return "Something went wrong. Try again."