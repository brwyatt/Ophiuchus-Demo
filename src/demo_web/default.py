import json

from ophiuchus.framework import Handler
from ophiuchus.framework import route


@route("/")
class Default(Handler):
    def GET(self, event, context):
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": "\n".join(
                [
                    "<html>",
                    "<head>",
                    "<title>Ophiuchus Demo</title>",
                    "</head>",
                    "<body>",
                    "<h1>Ophiuchus Demo</h1>",
                    "<h2>Running Endpoints</h2>",
                    "<ul>",
                    "\n".join(
                        [
                            f'<li><a href="{endpoint}">{name}</a></li>'
                            for name, endpoint in self.config.endpoint_map.items()
                        ],
                    ),
                    "</ul>",
                    "</body>",
                    "</html>",
                    "",
                ],
            ),
        }
