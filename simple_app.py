from flask import Flask


app = Flask(__name__) #use current namespace i.e. refer to yourself
app.run(debug=True, port=5000, host = '0.0.0.0')
