from peewee import *
from flask.ext.login import UserMixin
import datetime

#database
DATABASE = SqliteDatabase('social.db')

#define User class that imports from Model in peewee and UserMixin from flask-login
class User(UserMixin, Model):
    #define user attributes
    username = CharField(unique = True) #no users with the same username
    email_address = CharField(unique = True) #one account per email address
    password = CharField(max_length = 100)
    joined_at = DateTimeField(default = datetime.datetime.now) #no () after now, don't want time when script runs
    is_admin = BooleanField(default = False)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',) #'-' tells to sort users in descending order so most recent shown first