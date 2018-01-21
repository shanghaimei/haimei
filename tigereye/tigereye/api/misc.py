from flask_classy import FlaskView

class MiscView(FlaskView):
    def check(self):
        return "i'm ok"