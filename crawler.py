import requests
from datetime import date
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.live_info import LiveInfoModel
from models.musician import MusicianModel
from repositories.tables import Session
from repositories.tables import LiveInfo
from repositories.tables import UpdatedLiveInfo
from repositories.tables import Musician
from htmllaundry import sanitize
import schedule
import time
import os
import pdb
import re

def crawl():
  session = Session()
  musicians = session.query(Musician).all()

  for musician in musicians:
    musician_id = musician.id
    musician_url = musician.live_info_url

    resp = requests.get(musician_url).text
    try:
        soup = sanitize(BeautifulSoup(resp, "lxml").get_text())
    except:
        soup = sanitize(BeautifulSoup(resp, "html5lib").get_text())

    content = LiveInfo(
                musician_id=musician_id,
                content=soup,
                created_at=date.today())

    session.add(content)

  session.commit()
  arrange_updates()


def arrange_updates():
  session = Session()
  musicians = session.query(Musician).all()
  musician_ids = list(map(lambda m: m.id, musicians))

  for musician_id in musician_ids:
    live_info = session \
                .query(LiveInfo) \
                .filter(LiveInfo.musician_id == musician_id) \
                .order_by(LiveInfo.created_at.desc()) \
                .all()

    live_info_today = str(live_info[0].content)
    live_info_yesterday = str(live_info[1].content)

    live_info_diff = "".join(re.findall(
                     r'(.*\(.*\);.*|.*\{.*\}.*|.+=.+;|\n{2,}|<[a-z]+>)',
                     live_info_today.replace(live_info_yesterday, "")
                     ))
    today = live_info[0].created_at

    if live_info_diff == "":
      continue

    content = UpdatedLiveInfo(
      musician_id=musician_id,
      content=live_info_diff,
      created_at=today)

    session.add(content)

  session.commit()

schedule.every().day.at("0:30").do(crawl)

while True:
    schedule.run_pending()
    time.sleep(1)
