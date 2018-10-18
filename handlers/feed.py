from typing import Callable, List, Optional, Any

from tornado.web import HTTPError
from tornado_json.requesthandlers import ViewHandler
from repositories.tables import LiveInfo
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (Column, String, Text, ForeignKey, \
                create_engine, MetaData, DECIMAL, DATETIME, exc, event, Index)
import os

class FeedHandler(ViewHandler):
  def initialize(self, **config):
    pass

  def get(self, *args, **kwargs):
    # TODO: Sessionの定義をまとめる
    USER = "root"
    PW = ""
    HOST = "localhost"
    DB = "live_info_reader"
    PW = os.environ['LIVE_INFO_PASSWORD']
    DATABASE = f'mysql://{USER}:{PW}@{HOST}/{DB}?charset=utf8'
    ENGINE = create_engine(
        DATABASE,
        encoding="utf-8"
    )
    Session = sessionmaker(bind=ENGINE)

    session = Session()

    musicians = session.query(Musician).all()      
    return self.render("../templates/musicians.html", musicians=musicians)
