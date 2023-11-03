from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/sent', methods=["POST", "GET"])
def sent():
    if request.method == "POST":
        entry = request.form.get('entry_field')
        with open("Flask_ex99\\file.txt", "a+") as file:
            file.write(entry+"\n")
        return redirect(url_for('sent'))
    return render_template('home.jinja2')

@app.route('/')
def home():
    return render_template('home.jinja2')

if __name__ == '__main__':
    app.run(debug=True)