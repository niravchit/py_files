from flask import Flask, request, render_template


app = Flask(__name__) #use current namespace i.e. refer to yourself

#route
@app.route('/')
@app.route('/<name>') #capture text after / as value for name arg. Don't need request.args.get('name',name) now
def index(name = 'Nirav'):
    return render_template('index.html', name=name)

@app.route('/add/<int:num1>/<int:num2>') #type conversion in url by flask
def add(num1, num2):
    context = {'num1':num1, 'num2':num2} #key value pairings tying variables in view to those in html template
    return render_template('add.html', **context) #pass template name, plus key:value associations for variables

app.run(host = '127.0.0.1', port = 5000, debug=True)
