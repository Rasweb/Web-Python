from flask import Flask, render_template, session, request # type: ignore
# app = Flask(__name__)
app = Flask(__name__, 
            template_folder='../frontend/templates',
            static_folder='../frontend/static')
app.secret_key = 'myKey'
# post

# Store password in session
#        session['password'] = password

# Retrieve password from session
#    password = session.get('password')

@app.route("/")
def actions():
    print("Hello")
    return render_template("index.html")


@app.route("/create")
def createPasswords():
    if request.method == 'POST':
    
        return 'Password created successfully!'
    return render_template("create/create.html")

@app.route("/view")
def viewPasswords():
    return "Here you can view your passwords"

@app.route("/update")
def updatePasswords():
    return "Here you can update your passwords"
    # Edit passwords
    # Create passwords
    # Remove passwords
    # Showing passwords

@app.route("/remove")
def removePasswords():
    return "Here you can delete your passwords"

