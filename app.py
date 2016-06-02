from flask import Flask, render_template, redirect, url_for, \
    request
from forms import ContactForm
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

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


@app.route('/blogs')
def Blogs():
    return 'Blogs undergoing maintainance. Please check back later'


@app.route('/about')
def About():
    return render_template('/public_access/about.html')


@app.route('/contact', methods=['GET', 'POST'])
def Contact():
    error = None
    form = ContactForm(request.form)
    return render_template('/public_access/contact.html', error=error, form=form)



if __name__ == "__main__":
    app.run(debug=True)
