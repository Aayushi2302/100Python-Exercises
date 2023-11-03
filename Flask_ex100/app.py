from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/sent', methods=["POST", "GET"])
def sent():
    if request.method == "POST":
        username = request.form.get('username')
        with open("Flask_ex100\\username.txt", "r") as file:
            file.seek(0)
            usernames = file.readlines()
            usernames = [username.strip("\n") for username in usernames]
            if username in usernames:
                return render_template('home.jinja2', prompt = "Username already exist")
        
        password = request.form.get('password')
        regex_num_pattern = '[0-9]+'
        regex_caps_pattern = '[A_Z]+'
        is_pass_num = re.search(regex_num_pattern, password)
        is_pass_caps = re.search(regex_caps_pattern, password)
        password_length = len(password) >= 5
        
        if is_pass_caps and is_pass_num and password_length:
            with open("Flask_ex100\\username.txt", "a+") as file:
                file.writelines(username)
            with open("Flask_ex100\\password.txt", "a+") as file:
                file.writelines(password)
            return render_template('home.jinja2', prompt = "Success")
        else:
            return render_template('home.jinja2', prompt = "Please check your password")
        
    return render_template('home.jinja2')

@app.route('/')
def home():
    return render_template('home.jinja2')

if __name__ == "__main__":
    app.run(debug = True)