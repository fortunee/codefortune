#############
## Imports ##
#############

from flask import Flask, render_template, redirect, url_for, \
    request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail
import os

##################################
### initializing the flask app ###
### setting up the mail config ###
##################################


mail = Mail()

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ['EMAIL']
app.config["MAIL_PASSWORD"] = os.environ['PASSWORD']

mail.init_app(app)

############
## Routes ##
############


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
    return render_template('/public_access/blogs.html')


@app.route('/about')
def About():
    return render_template('/public_access/about.html')


@app.route('/contact', methods=['GET', 'POST'])
def Contact():
    error = None
    form = ContactForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                msg = Message(
                    form.subject.data,
                    sender=form.email.data,
                    recipients=[
                        os.environ['EMAIL'],
                        os.environ['SECOND_EMAIL'],
                        os.environ['THIRD_EMAIL']])
                msg.body = """
                From: %s <%s>
                %s
                """ % (form.name.data, form.email.data, form.message.data)
                mail.send(msg)
                flash("Your message has been sent. Thanks, I'll be in touch")
                return redirect(url_for('Contact'))
            except:
                error = 'Please check your internet connection and try again'
                return render_template(
                    '/public_access/contact.html', error=error, form=form
                )
        else:
            error = """Please check the form for the incorrect detail(s) \
                and resend. Thanks"""
            return render_template(
                '/public_access/contact.html', error=error, form=form
            )
    elif request.method == 'GET':
        return render_template('/public_access/contact.html', form=form)

if __name__ == "__main__":
    app.run()
