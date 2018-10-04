# -*- coding: utf-8 -*-

from handlers.musician import MusicianHandler

def get_routes(**kwargs):
    routes = [
        ('/?', IndexHandler, kwargs),
        ('/musisians/?', MusiciansHandler, kwargs),
    ]
    return routes
