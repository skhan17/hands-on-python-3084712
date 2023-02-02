from distutils.log import debug
from flask import Flask

# instantiate Flask object called app
app = Flask(__name__)

# define route
@app.route("/")
def hello():
  return "Hello, World!"

app.run(debug=True)
