#routers
from app.app import api, app, login_manager
from app.models.usermodel import User
from app.views.Userregistration import userregister,userlogin
from app.views.orderitem import orderitem,orderupdate
from app.views.hotelupdate import hotelupdate
from app.views.admin import admin
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user):
    """current user details"""
    return User.objects.get(id=user)
#for login
app.add_url_rule("/", view_func=userlogin, methods=["GET","POST"])
#for user register
app.add_url_rule("/register",view_func=userregister,methods=["GET","POST"])
#for ordering item
app.add_url_rule("/orderitem",view_func=orderitem,methods=["GET","POST"])
#for order update and it is available only for delivery user
app.add_url_rule("/orderupdate",view_func=orderupdate,methods=["GET","POST"])
app.add_url_rule("/admin", view_func=admin, methods=["GET","POST"])
app.add_url_rule("/hotelupdate", view_func=hotelupdate, methods=["GET","POST"])