
import asyncio
import logging

import tornado.httpclient
import tornado.web


logger = logging.getLogger(__name__)


class MainHandler(tornado.web.RequestHandler):

    async def get(self):

        await asyncio.sleep(1)

        http = tornado.httpclient.AsyncHTTPClient()
        response = await http.fetch("http://google.com/")

        self.write(f'Downloaded! status code: {response.code}')



