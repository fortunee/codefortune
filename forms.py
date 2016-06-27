from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

# contact form populated by flask wtform


class ContactForm(Form):
    name = TextField(
        'name', validators=[DataRequired(), Length(min=3, max=45)]
    )
    email = TextField(
        'email', validators=[
            DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    subject = TextField(
        'subject', validators=[
            DataRequired(), Length(min=3, max=60)]
    )
    message = TextAreaField(
        'message', validators=[
            DataRequired(), Length(min=8, max=290)]
    )
