from tigereye.models import db,Model
from tigereye.models.seat import SeatStatus


class Cinema(db.Model,Model):
    #cid 影院id,主键
    cid = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True,nullable=False)
    address = db.Column(db.String(128),nullable=False)
    halls = db.Column(db.Integer,default=0,nullable=False)
    handle_fee = db.Column(db.INTEGER,default=0,nullable=False)
    buy_limit = db.Column(db.INTEGER,default=0,nullable=False)
    status = db.Column(db.INTEGER,default=0,nullable=False,index=True)

    @classmethod
    def create_test_data(cls,cinema_num = 3,hall_num = 3,play_num = 10):
            import  time


            from tigereye.models.hall import Hall
            from tigereye.models.seat import Seat,PlaySeat,SeatType
            from tigereye.models.movie import Movie
            from tigereye.models.cinema import Cinema
            from tigereye.models.play import Play
            from faker import Faker
            import math
            from datetime import datetime
            start_time = time.time()
            HALL_SEATS_NUM = 25
            faker = Faker('zh_CN')
            cinemas = []
            for i in range(1,cinema_num+1):
                cinema = Cinema()
                cinema.name = '%s影城' % faker.name()
                cinema.address = faker.address()
                cinema.status = 1
                cinema.put()
                cinemas.append(cinema)
            Cinema.commit()
            halls = []
            plays = []

            for cinema in cinemas:
                for n in range(1,hall_num+1):
                    hall = Hall()
                    hall.cid = cinema.cid
                    hall.name = '%s 号厅' % n
                    hall.screen_type = "IMAX"
                    hall.audio_type = '杜比环绕'
                    hall.seats_num = HALL_SEATS_NUM
                    hall.status = 1
                    hall.put()
                    halls.append(hall)
                Hall.commit()

            for hall in halls:
                hall.seats = []


                for x in range(1,HALL_SEATS_NUM+1):
                    seat = Seat()
                    seat.cid = hall.cid
                    seat.hid = hall.hid
                    seat.x = x % 5 or 5
                    seat.y = math.ceil(x / 5)
                    seat.row = '%s 排' % seat.x
                    seat.column = '%s 列' % seat.y
                    seat.seat_type = SeatType.single.value

                    seat.status = SeatStatus.ok.value
                    seat.put()
                    hall.seats.append(seat)
                Seat.commit()



                for p in range(1,play_num+1):
                     play = Play()
                     play.cid = hall.cid
                     play.hid = hall.hid
                     play.mid = p
                     play.start_time = datetime.now()
                     play.duration = 3600
                     play.price_type = 1
                     play.price = 70000
                     play.market_price = 5000
                     play.lowest_price = 3000
                     play.status = 1
                     play.put()
                     play.hall = hall
                     plays.append(play)
                Play.commit()
            for play in plays:


                for seat in play.hall.seats:
                     ps = PlaySeat()
                     ps.pid = play.pid
                     ps.copy(seat)
                     ps.put()


                PlaySeat.commit()


            for i in range(10):
                m = Movie()
                m.name = '电影名称 %s' % (i +1)
                m.language = '英文'
                m.subtitle = '中文'
                m.mode = '数字'
                m.vision = '3D'
                m.screen_size = 'IMAX'
                m.introduction = '哈哈哈'
                m.status = 1
                m.save()
            print('create test data done! cost %s seconds' % (time.time() - start_time))