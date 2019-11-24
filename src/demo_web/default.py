from ophiuchus.framework import Handler
from ophiuchus.framework import route


@route("/")
class Default(Handler):
    pass
