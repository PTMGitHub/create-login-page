####################################################################
##############        Import packages        #######################
####################################################################
from flask import Blueprint, render_template, redirect, url_for, \
request, flash
from werkzeug.security \
import generate_password_hash, check_password_hash
##from models import User
from flask_login import login_user, logout_user, \
login_required, current_user
from __init__ import db
####################################################################
auth = Blueprint('auth', __name__) # create a Blueprint object that
# we name 'auth'
####################################################################
@auth.route('/login', methods=['GET']) # define login page path
def login(): # define login page fucntion
  return 'login'
####################################################################
@auth.route('/signup', methods=['GET'])# we define the sign up path
def signup(): # define the sign up function
  return 'signup'
####################################################################
@auth.route('/logout') # define logout path
def logout(): #define the logout function
  return 'logout'
