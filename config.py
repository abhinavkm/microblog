import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
#flask-wtf uses SECRET_KEY to protect web forms again CSRF attacks
