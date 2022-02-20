from app.app import login_manager
from app.models.usermodel import User
from app.models.hotel import Hotels
from flask_restful import Resource
from app.views.orderitem import orderitem

from flask import jsonify,request,flash,render_template,redirect, url_for
from flask_login import current_user,LoginManager,login_required,login_user,logout_user

def hotelupdate():
    if request.method=='POST':
        if "Add" in request.form:
            hotelid = request.form["hotelid"]
            hotelname = request.form["hotelname"]
            hoteladdress = request.form["hoteladdress"]
            hotelphone = request.form["hotelphone"]
            Hotels.objects.create(hotelid=hotelid,hotelname=hotelname,hoteladdress=hoteladdress,hotelphone=hotelphone)
        elif "Delete" in request.form:
            Hotels.objects(hotelid=request.form["hotelid"]).delete()
        else:
            return redirect(url_for('admin'))
    
    hotels=Hotels.objects
    return render_template("hotelupdate.html",hotels=hotels)