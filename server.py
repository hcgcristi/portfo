from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

# @app.route('/<username>/<int:iduser>')
# def hello_world(username=None, iduser=None):
#   return render_template('index.html',name=username, iduser=iduser)

@app.route('/')
def my_home():
  return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
  return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv',mode='a', newline='') as databasecsv:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(databasecsv,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_file(data)
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'Salvarea a esuat!'
	else:	
		return 'ceva nu a mers bine'

# @app.route('/home.html')
# def home():
#   return my_home()

# @app.route('/about.html')
# def about():
#   return render_template('about.html')

# @app.route('/works.html')
# def works():
#   return render_template('works.html')

# @app.route('/work.html')
# def work():
#   return render_template('work.html')

# @app.route('/contact.html')
# def contact():
#   return render_template('contact.html')

# @app.route('/components.html')
# def componennts():
#   return render_template('components.html')

# @app.route('/blog')
# def blog():
#   return 'acesta e blogul!'  