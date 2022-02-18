from app.app import login_manager
from app.models.usermodel import User
from flask_restful import Resource
from app.views.orderitem import orderitem
from flask import jsonify,request,flash,render_template,redirect, url_for
from flask_login import current_user,LoginManager,login_required,login_user,logout_user

def admin():
    if request.method == 'POST':
        logout_user()
        return redirect(url_for('userlogin'))
    else:
        users=User.objects
        return render_template("admin.html",users=users)