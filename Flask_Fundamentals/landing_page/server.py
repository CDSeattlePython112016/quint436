from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "quintskey"

@app.route('/')
def index():
  return render_template("index.html")


@app.route('/process', methods=['POST'])
def submit_info():
    name = request.form['name']
    location = request.form['location']
    lang = request.form['lang']
    comment = request.form['comment']
    return render_template("results.html", name=name, loc=location, lang=lang, cum=comment)

app.run(debug=True)
