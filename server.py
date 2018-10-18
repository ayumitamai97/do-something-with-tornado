# -*- coding: utf-8 -*-
# import tornado.ioloop
# import tornado.web
import tornado.wsgi
import wsgiref.simple_server
from handlers.musician import MusicianHandler
from handlers.feed import FeedHandler
import schedule
import time
import scraper

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/feed.html')

# scraper.crawl()
# schedule.every().day.at("0:50").do(scraper.crawl)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/musicians", MusicianHandler),
    (r"/feed", FeedHandler),
])

if __name__ == "__main__":
    wsgi_app = tornado.wsgi.WSGIAdapter(application)
    server = wsgiref.simple_server.make_server('', 8080, wsgi_app)
    server.serve_forever()
