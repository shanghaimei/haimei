from flask import jsonify
from flask_classy import FlaskView
from tigereye.models.cinema import Cinema

class CinemaView(FlaskView):


    def all(self):
        cinemas = Cinema.query.all()
        cinema_list = []
        for cinema in cinemas:
            cinema_list.append({
                'cid':cinema.cid,
                'name':cinema.name,
                'address':cinema.address,
                'halls':cinema.halls,
                'handle_fee':cinema.handle_fee,
                'buy_limit':cinema.buy_limit,
                'status':cinema.status,
            })
        return jsonify(cinema_list)