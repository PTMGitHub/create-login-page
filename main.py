####################################################################
###############         Import packages          ###################
####################################################################
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app

####################################################################
# our main blueprint
main = Blueprint("main", __name__)
####################################################################
@main.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


####################################################################
@main.route("/profile")  # profile page that return 'profile'
def profile():
    return render_template("profile.html")


####################################################################
app = create_app()  # we initialize our flask app using the
# __init__.py function
####################################################################
if __name__ == "__main__":
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True)  # run the flask app on debug mode
