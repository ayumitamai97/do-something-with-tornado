# -*- coding: utf-8 -*-
# import tornado.ioloop
# import tornado.web
import tornado.wsgi
import wsgiref.simple_server
from handlers.musician import MusicianHandler
from handlers.feed import FeedHandler
import schedule
import time
import crawler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/feed.html')

# crawler.crawl()
# schedule.every().day.at("0:50").do(crawler.crawl)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/musicians", MusicianHandler),
    (r"/feed", FeedHandler),
])

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

    wsgi_app = tornado.wsgi.WSGIAdapter(application)
    server = wsgiref.simple_server.make_server('', 8080, wsgi_app)
    server.serve_forever()
