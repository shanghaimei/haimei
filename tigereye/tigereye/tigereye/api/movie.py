from flask import request
from tigereye.api import ApiView
from tigereye.models.movie import Movie
from tigereye.extensions.validator import Validator
class MovieView(ApiView):
    def all(self):

        return Movie.query.all()

    @Validator(mid = int)
    def get(self):

        mid = request.params['mid']
        movie = Movie.get(mid)

        return movie

