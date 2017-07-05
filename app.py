
import logging
import tornado.web

import handlers
import settings


logger = logging.getLogger(__name__)


def get_app():
    return tornado.web.Application(
        handlers=[
            (r"/", handlers.MainHandler),
        ]
    )

async def run():
    application = get_app()
    application.listen(settings.APP.get('port', 8000))



