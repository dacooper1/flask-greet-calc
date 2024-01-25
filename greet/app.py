# In the ***greet*** folder, Make a simple Flask app that responds to these routes with simple text messages:

# ***/welcome***   Returns “welcome”

# ***/welcome/home***   Returns “welcome home”

# ***/welcome/back***   Return “welcome back”

from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "<h1>Welcome</h1>"

@app.route('/welcome/home')
def welcome_home():
    return "<h1>Welcome Home</h1>"

@app.route('/welcome/back')
def welcome_back():
    return "<h1>Welcome Back</h1>"
