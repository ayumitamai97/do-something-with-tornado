import requests
from datetime import date
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.live_info import LiveInfoModel
from models.musician import MusicianModel
from repositories.tables import LiveInfo
from repositories.tables import Musician
import schedule
import time
import os

def crawl():
    # TODO まとめる
    # TODO 環境変数名をもう少しわかりやすく
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

    for musician in musicians:
        musician_id = musician.id
        musician_url = musician.live_info_url

        resp = requests.get(musician_url).text
        try:
            soup = remove_tags(BeautifulSoup(resp, "lxml").get_text())
        except:
            soup = remove_tags(BeautifulSoup(resp, "html5lib").get_text())

        content = LiveInfo(
                    musician_id=musician_id,
                    content=soup,
                    created_at=date.today())

        session.add(content)

    session.commit()

# schedule.every().day.at("0:30").do(crawl)
schedule.every().minute.do(crawl)

while True:
    schedule.run_pending()
    time.sleep(1)
