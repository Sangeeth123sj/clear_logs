from flask import Blueprint
from flask_login import login_user, logout_user,current_user,login_required

views = Blueprint('views', __name__)

@views.route('/blueprint_test')
def blues():
    return "<h1>Test worked </h1>"
