from flask import Flask, render_template, request, flash

app = Flask(__name__)

app.secret_key = "development key"

def contact():
    name = form.name
    email = form.name
    subject = form.subject
    message = form.message