# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.wsgi
import wsgiref.simple_server
from handlers.musician import MusicianHandler
from handlers.feed import FeedHandler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/feed.html')


application = tornado.web.Application([
    (r"/", FeedHandler),
    (r"/feed", FeedHandler),
    (r"/musicians", MusicianHandler),
])

if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()
