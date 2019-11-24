import json

from ophiuchus.framework import Handler
from ophiuchus.framework import route


@route("/")
class Default(Handler):
    def GET(self, event, context):
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
            },
            'body': json.dumps({"message": "yup, hi!"})
        }
