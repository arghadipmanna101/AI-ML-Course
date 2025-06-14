from flask import Flask,render_template

'''
It creates an instance of the Flask class, which will be your WSGI(Web Server Gatway Interface) application.
'''
# WSGI Application
app=Flask(__name__)

@app.route("/welcome")
def Welcome():
    return render_template("welcome.html")

@app.route("/index",method=['GET'])
def Index():
    return render_template("index.html")

@app.route("/about")
def About():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)