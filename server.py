# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
from handlers.musician import MusicianHandler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/feed.html')

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/musicians", MusicianHandler),
    (r"/feed", FeedHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
