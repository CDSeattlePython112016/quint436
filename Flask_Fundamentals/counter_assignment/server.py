from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'quint'

@app.route('/')
def index():

    if 'times' not in session:
        session['times'] = 0
    session['times'] = session['times'] + 1
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():

    session['times'] = session['times'] + 1#if button is clicked, session [times] += 2
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['times'] = 0
    return redirect('/')
app.run(debug=True)
