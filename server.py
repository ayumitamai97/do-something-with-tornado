# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
from handlers.musician import MusicianHandler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/musicians", MusicianHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
