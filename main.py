####################################################################
###############         Import packages          ###################
####################################################################
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app
####################################################################
# our main blueprint
main = Blueprint('main', __name__)
####################################################################
@main.route('/') # home page that return 'index'
def index():
  return 'index'
####################################################################
@main.route('/profile') # profile page that return 'profile'
def profile():
  return 'profile'
####################################################################
app = create_app() # we initialize our flask app using the
#__init__.py function
####################################################################
if __name__ == '__main__':
  app.run(debug=True) # run the flask app on debug mode
