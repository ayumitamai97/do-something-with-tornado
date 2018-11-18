from typing import Callable, List, Optional, Any

from tornado.web import HTTPError
from tornado_json.requesthandlers import ViewHandler
from repositories.tables import Musician
from repositories.tables import LiveInfo
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (Column, String, Text, ForeignKey, \
                create_engine, MetaData, DECIMAL, DATETIME, exc, event, Index)
import os
import pdb

class FeedHandler(ViewHandler):
  def initialize(self, **config):
    pass

  def get(self, *args, **kwargs):
    # TODO: Sessionの定義をまとめる
    USER = "root"
    HOST = os.environ['DB_HOSTNAME']
    DB = "live_info_crawler"
    PW = os.environ['LIVE_INFO_PASSWORD']
    DATABASE = f'mysql://{USER}:{PW}@{HOST}/{DB}?charset=utf8'
    ENGINE = create_engine(
        DATABASE,
        encoding="utf-8"
    )
    Session = sessionmaker(bind=ENGINE)
    session = Session()

    musicians = session.query(Musician).all()
    musician_ids = list(map(lambda m: m.id, musicians))

    all_live_info = {}

    for musician_id in musician_ids:
      live_info = session.query(LiveInfo).filter(LiveInfo.musician_id == musician_id).all()
      live_info_today = str(live_info[0].content)
      live_info_yesterday = str(live_info[1].content)
      live_info_diff = live_info_today.replace(live_info_yesterday, "")
      all_live_info[musician_id] = live_info_diff

      # pdb.set_trace() # debugger

    return self.render("../templates/feed.html", live_info=live_info)
