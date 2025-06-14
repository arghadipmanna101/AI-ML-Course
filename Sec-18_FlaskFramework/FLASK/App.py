from flask import Flask

'''
It creates an instance of the Flask class, which will be your WSGI(Web Server Gatway Interface) application. 
'''
# WSGI Application
app=Flask(__name__)

@app.route("/welcome")
def Welcome():
    return "Welcome to our server."

@app.route("/index")
def Index():
    return "Welcome to the index page."

if __name__=="__main__":
    app.run(debug=True)