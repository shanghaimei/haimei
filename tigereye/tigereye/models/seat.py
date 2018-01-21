from tigereye.models import db,Model

class Seat(db.Model,Model):

    """座位id"""
    sid = db.Column(db.INTEGER,primary_key=True)
    """影厅id"""
    hid = db.Column(db.INTEGER)
    """影院id"""
    cid = db.Column(db.INTEGER)

    x = db.Column(db.INTEGER,default=0,nullable=False)
    y = db.Column(db.INTEGER, default=0,nullable=False)
    """显示行名称"""
    row = db.Column(db.String(8))
    """显示列名称"""
    column = db.Column(db.String(8))

    area = db.Column(db.String(16))
    seat_type = db.Column(db.String(16))
    love_seats = db.Column(db.String(32))
    status = db.Column(db.INTEGER,default=0,nullable=False,index=True)