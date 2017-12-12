from flask import (Flask, request, render_template, redirect, request, url_for, make_response)
import simplejson as json

app = Flask(__name__) #use current namespace i.e. refer to yourself

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('apple_product')) #get saved data cookies
    except TypeError:
        data = {} #empty dict in case no cookies
    print data
    return data

#routes
@app.route('/')
@app.route('/<name>') #capture text after / as value for name arg. Don't need request.args.get('name',name) now
def index(name = 'Nirav'):
    data = get_saved_data() #get saved data
    return render_template('index.html', saves = data) #set data to saves variable in index.html

@app.route('/add/<int:num1>/<int:num2>') #type conversion in url by flask
def add(num1, num2):
    context = {'num1':num1, 'num2':num2} #key value pairings tying variables in view to those in html template
    return render_template('add.html', **context) #pass template name, plus key:value associations for variables

@app.route('/save', methods = ['POST']) #only accessible with POST methods
def save():
    response = make_response(redirect(url_for('index'))) #generate a response to pass in cookie without returning
    data = get_saved_data()
    data.update(dict(request.form.items())) #update data if need to 
    response.set_cookie('apple_product', json.dumps(data)) #set cookie
    return response

app.run(host = '127.0.0.1', port = 5000, debug=True)
