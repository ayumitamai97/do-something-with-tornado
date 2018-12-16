# -*- coding: utf-8 -*-
from typing import Callable, List, Optional, Any

from tornado.web import HTTPError
from tornado_json.requesthandlers import ViewHandler
from repositories.tables import Musician
from repositories.tables import Session
import os


class MusicianHandler(ViewHandler):
  def initialize(self, **config):
    pass

  def get(self, *args, **kwargs):
    session = Session()

    musicians = session.query(Musician).all()      
    return self.render("../templates/musicians.html", musicians=musicians)

  def post(self, *args, **kwargs):
    musician_name = self.get_body_argument("name")
    musician_url = self.get_body_argument("url")
    musician = Musician(name=musician_name, live_info_url=musician_url)

    session = Session()
    session.add(musician)
    session.commit()

    musicians = session.query(Musician).all()

    self.redirect("/musicians")
