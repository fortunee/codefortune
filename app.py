from flask import Flask, render_template, redirect, url_for \

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/learn_more')
def LearnMore():
    return render_template('learn_more_clicked.html')

@app.route('/projects')
def Projects():
    return render_template('/public_access/projects.html')

if __name__ == "__main__":
    app.run(debug=True)
