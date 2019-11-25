import json

from ophiuchus.framework import Handler
from ophiuchus.framework import route


@route(r"/debug")
@route(r"/debug/{proxy+}")
class Debug(Handler):
    def GET(self, event, context):
        return self._all(event, context)

    def POST(self, event, context):
        return self._all(event, context)

    def PUT(self, event, context):
        return self._all(event, context)

    def DELETE(self, event, context):
        return self._all(event, context)

    def _all(self, event, context):
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": "\n".join(
                [
                    "<html>",
                    "<head>",
                    "<title>DEBUG</title>",
                    "</head>",
                    "<body>",
                    "<h1>DEBUG</h1>",
                    "<h2>EVENT DETAILS</h2>",
                    "<pre>",
                    f"{json.dumps(event, indent=4, sort_keys=True)}",
                    "</pre>",
                    "</body>",
                    "</html>",
                    "",
                ],
            ),
        }
