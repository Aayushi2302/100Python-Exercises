from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
    
   if request.method == "POST":
      pass
   return render_template('home.jinja2')

if __name__ == '__main__':
    app.run(debug=True)