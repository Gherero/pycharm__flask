__author__ = 'kiro'
from wtforms import Form,BooleanField,TextField,PasswordField,validators

class Registform(Form):
    name=TextField('Name',[validators.Length(min=2,max=60)])
    lastname=TextField('Lastname',[validators.Length(min=2,max=60)])
    internet=BooleanField('internet')
    mail=BooleanField('mail')
    file_server=BooleanField('file_server')

