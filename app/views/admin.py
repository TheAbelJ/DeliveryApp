from app.app import login_manager
from app.models.usermodel import User
from app.models.hotel import Hotels
from flask_restful import Resource
from app.views.orderitem import orderitem
from flask import jsonify,request,flash,render_template,redirect, url_for
from flask_login import current_user,LoginManager,login_required,login_user,logout_user
from app.views.hotelupdate import hotelupdate

def admin():
    if request.method == 'POST':
        if 'HotelUpdate' in request.form:
            return redirect(url_for('hotelupdate'))
        else:
            logout_user()
            return redirect(url_for('userlogin'))
    else:
        users=User.objects
        hotels=Hotels.objects
        return render_template("admin.html",users=users,hotels=hotels)