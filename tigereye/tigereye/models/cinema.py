from tigereye.models import db,Model

class Cinema(db.Model,Model):
    #cid 影院id,主键
    cid = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True,nullable=False)
    address = db.Column(db.String(128),nullable=False)
    halls = db.Column(db.Integer,default=0,nullable=False)
    handle_fee = db.Column(db.INTEGER,default=0,nullable=False)
    buy_limit = db.Column(db.INTEGER,default=0,nullable=False)
    status = db.Column(db.INTEGER,default=0,nullable=False,index=True)