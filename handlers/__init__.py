# -*- coding: utf-8 -*-

from handlers.musician import MusicianHandler

def get_routes(**kwargs):
    routes = [
        ('/?', FeedHandler, kwargs),
        ('/musisians/?', MusiciansHandler, kwargs),
    ]
    return routes
