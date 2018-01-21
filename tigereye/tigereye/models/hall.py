from tigereye.models import db,Model


class Hall(db.Model,Model):
    hid = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer)
    name = db.Column(db.String(64), unique=True, nullable=False)

    screen_type = db.Column(db.String(32))
    audio_type = db.Column(db.String(32))
    seats_num = db.Column(db.INTEGER,default=0,nullable=False,index=True)