
from tigereye.api import ApiView

class testView(ApiView):
    def error(self):
        1/0


