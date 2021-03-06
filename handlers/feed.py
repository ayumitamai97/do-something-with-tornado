from typing import Callable, List, Optional, Any

from tornado.web import HTTPError
from tornado_json.requesthandlers import ViewHandler
from repositories.tables import Session
from repositories.tables import Musician
from repositories.tables import UpdatedLiveInfo
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (Column, String, Text, ForeignKey, \
                create_engine, MetaData, DECIMAL, DATETIME, exc, event, Index)
import os
import re
import pdb # python debugger

class FeedHandler(ViewHandler):
  def initialize(self, **config):
    pass

  def get(self, *args, **kwargs):
    session = Session()

    musicians_query = session.query(Musician)
    musicians = musicians_query.all()
    musician_ids = list(map(lambda m: m.id, musicians))

    all_live_info = {}

    for musician_id in musician_ids:
      musician_name = musicians_query.filter(Musician.id == musician_id).first().name
      live_info_list = session \
                        .query(UpdatedLiveInfo) \
                        .filter(UpdatedLiveInfo.musician_id == musician_id) \
                        .order_by(UpdatedLiveInfo.created_at.desc()) \
                        .all()

      for live_info in live_info_list:
        created_at = str(live_info.created_at)
        jscontent = re.findall(r'(.*\(.*\);.*|.*\{.*\}.*|.+=.+;|\n{2,}|<[a-z]+>)', live_info.content)
        content = live_info.content

        if not jscontent == []:
          for jscont in jscontent:
            content = content.replace(jscont, "")

      if created_at in all_live_info:
        all_live_info[created_at].append({ musician_name: content })
      else:
        all_live_info[created_at] = [{ musician_name: content }]

    return self.render("../templates/feed.html", live_info=all_live_info)
