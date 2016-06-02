from flask import Flask, render_template, redirect, url_for, \
    request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail
import os

#initializing the flask app
#setting up the config
mail = Mail()

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ['EMAIL']
app.config["MAIL_PASSWORD"] = os.environ['PASSWORD']

mail.init_app(app)

#mapping for the index and home page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#mapping the learn more page
@app.route('/learn_more')
def LearnMore():
    return render_template('learn_more_clicked.html')

#mapping the projects page
@app.route('/projects')
def Projects():
    return render_template('/public_access/projects.html')

#mapping the blogs page
@app.route('/blogs')
def Blogs():
    return 'Blogs undergoing maintainance. Please check back later'

#mapping the about page
@app.route('/about')
def About():
    return render_template('/public_access/about.html')

#mapping the contact page
@app.route('/contact', methods=['GET', 'POST'])
def Contact():
    error = None
    form = ContactForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            msg = Message(form.subject.data, sender=form.email.data, recipients=[os.environ['EMAIL']])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            flash("Your message has been sent. Thanks, I'll be in touch")
            return redirect(url_for('Contact'))
        else:
            error = "Please check the form for the incorrect detail(s) and resend. Thanks"
            return render_template('/public_access/contact.html',
                error=error, form=form)
    elif request.method == 'GET':
        return render_template('/public_access/contact.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)
