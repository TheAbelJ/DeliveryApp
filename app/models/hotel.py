from app.app import db

class Hotels(db.Document):
	hotelid=db.StringField(required=True)
	hotelname = db.StringField(required=True)
	hoteladdress = db.StringField(required=True)
	hotelphone = db.StringField()