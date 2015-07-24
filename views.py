__author__ = 'kiro'
from app import app
from forms import Registform
from flask import render_template

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.registration('/l',methods=['GET','POST'])
def registration():
    form = Registform
    name= form.name.data
    l_name=form.lastname.data
    file_server_access=form.file_server.data
    internet_access=form.internet.data
    mail_access=form.mail.data
    return render_template('register.html', form=form)


