from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my fully backend password manager using inputs"

# post
@app.route("/manage", methods = ['POST'])
def actions():
    print("Hello")
    #  Ask user using inputs for:
    # If they wish to see current passwords
    # Create a new password
    # Manage passwords

def currentPasswords():
    print("Showing your current passwords")

def createNewPassword():
    print("creating a new password")

def managePasswords():
    print("Managing passwords")
    # Edit passwords
    # Create passwords
    # Remove passwords
    # Showing passwords

