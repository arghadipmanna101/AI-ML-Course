# Variable rule

from flask import Flask, render_template, request

'''
It creates an instance of the Flask class, which will be your WSGI(Web Server Gateway Interface) application.
'''
# WSGI Application
app = Flask(__name__)

@app.route("/welcome")
def Welcome():
    return render_template("welcome.html")

@app.route("/index")
def Index():
    return render_template("index.html")

@app.route("/about")
def About():
    return render_template("about.html")

@app.route('/submit', methods=['GET', 'POST'])  # Fixed typo
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name} !'
    return render_template('form.html')

#Variable Rule :
@app.route("/success/<int:score>")
def success(score):
    return "The marks you got is " +str(score)

if __name__ == "__main__":
    app.run(debug=True)
