import json

from ophiuchus.framework import Handler
from ophiuchus.framework import route


@route("/")
@route("/{test}")
class Default(Handler):
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
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',
            },
            'body': "\n".join([
                "<html><head><title>EVENT DETAILS</title><body>",
                "<h1>EVENT DETAILS</h1><pre>",
                f"{json.dumps(event, indent=4, sort_keys=True)}",
                "</pre></body></html>",
                "",
            ]),
        }
