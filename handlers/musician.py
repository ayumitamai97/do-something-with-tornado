# -*- coding: utf-8 -*-
from typing import Callable, List, Optional, Any

from tornado.web import HTTPError
from tornado_json.requesthandlers import ViewHandler
from repositories.tables import Musician

# TODO: まとめる
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (Column, String, Text, ForeignKey, \
                create_engine, MetaData, DECIMAL, DATETIME, exc, event, Index)


class MusicianHandler(ViewHandler):
  def initialize(self, **config):
    pass

  def get(self, *args, **kwargs):
    # TODO: Sessionの定義をまとめる
    USER = "root"
    PW = ""
    HOST = "localhost"
    DB = "live_info_reader"
    DATABASE = f'mysql://{USER}:{PW}@{HOST}/{DB}?charset=utf8'
    ENGINE = create_engine(
        DATABASE,
        encoding="utf-8"
    )
    Session = sessionmaker(bind=ENGINE)

    session = Session()

    musicians = session.query(Musician).all()      
    return self.render("../templates/musicians.html", musicians=musicians)

  def post(self, *args, **kwargs):
    musician_name = self.get_body_argument("name")
    musician_url = self.get_body_argument("url")
    musician = Musician(name=musician_name, live_info_url=musician_url)


    USER = "root"
    PW = ""
    HOST = "localhost"
    DB = "live_info_reader"
    DATABASE = f'mysql://{USER}:{PW}@{HOST}/{DB}?charset=utf8'
    ENGINE = create_engine(
        DATABASE,
        encoding="utf-8"
    )
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    session.add(musician)
    session.commit()

    musicians = session.query(Musician).all()

    self.redirect("/musicians")
