import uuid
from flask import jsonify,request,render_template,redirect, url_for
from flask_login import current_user
from app.models.usermodel import User
from app.models.orderdetailmodel import OrderDetails
def orderitem():
	#function for ordering item
	if request.method == 'POST':
		itemname = request.form["itemname"]
		pickupaddress = request.form["pickupaddress"]
		newaddress = request.form["newaddress"]
		deliveryaddress = request.form.get("deliveryaddress")
		print(deliveryaddress)
		if  newaddress:
			user =  User.objects.get(id=current_user.id)
			deliveryaddresslist = user.deliveryaddress
			deliveryaddresslist.append(newaddress)
			user.deliveryaddress = deliveryaddresslist
			user.save()
			deliveryaddress = newaddress
		else:
			deliveryaddress=deliveryaddress
		uniqueuid = uuid.uuid4().hex
		OrderDetails.objects.create(itemname=itemname,
			pickupaddress=pickupaddress,deliveryaddress=deliveryaddress,
			ordereduser = current_user.id,orderid=uniqueuid)
		user =  User.objects.get(id=current_user.id)
		orderitems = OrderDetails.objects(ordereduser=current_user.id)
		return render_template("order.html",user=user,orderitems=orderitems)
	else:
		user =  User.objects.get(id=current_user.id)
		orderitems = OrderDetails.objects(ordereduser=current_user.id)
		return render_template("order.html",user=user,orderitems=orderitems)
	

def orderupdate():
	#function for order update by delivery user 
	if request.method=='POST':
		if (current_user.userrole=="deliveryuser"):		
			orderid = request.form["orderid"]
			statusoforder = request.form["statusoforder"]
			locationofagent = request.form["locationofagent"]
			order = OrderDetails.objects.get(orderid=orderid)
			order.statusoforder = statusoforder
			order.deliveryusername = current_user.username
			order.locationofagent = locationofagent
			order.deliveryuserphoneno = current_user.userphoneno
			order.save()
			orderitems=OrderDetails.objects
			return render_template("deliveryupdate.html",orderitems=orderitems)
			
		else:
			return render_template("login.html")
	else:
		if (current_user.userrole=="deliveryuser"):	
			orderitems=OrderDetails.objects
			return render_template("deliveryupdate.html",orderitems=orderitems)
		else:
			return render_template("login.html")
