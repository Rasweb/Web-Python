from flask import Flask, request # type: ignore
app = Flask(__name__)

# post
@app.route("/")
def actions():
    print("Hello")
    #  Ask user using inputs for:
    # If they wish to see current passwords
    # Create a new password
    # Manage passwords
    # return "Welcome to my fully backend password manager using inputs"

    return """
    <h1>Welcome to my Python password manager CRUD application!</h1>
    <p>Choose what you wish to do:</p>
    <ul>
        <li><a href="/create">Create a new password</a></li>
        <li><a href="/view">View all passwords</a></li>
        <li><a href="/update">Update the passwords</a></li>
        <li><a href="/remove">Remove passwords</a></li>
    </ul>
    """

@app.route("/create")
def createPasswords():
    return "Here you can create passwords"

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

if __name__ == '__main__':
    app.run(debug=True)