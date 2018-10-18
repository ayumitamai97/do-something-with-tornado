# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
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
    server = tornado.httpserver.HTTPServer(application)
    server.bind(8888)
    server.start(0)  # forks one process per cpu
    tornado.ioloop.IOLoop.current().start()
