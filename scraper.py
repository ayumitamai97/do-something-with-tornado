import requests
from datetime import date
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.live_info import LiveInfoModel
from models.musician import MusicianModel
from repositories.tables import LiveInfo
from repositories.tables import Musician

def crawl():
    # TODO まとめる
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

    for musician in musicians:
        musician_id = musician.id
        musician_url = musician.live_info_url

        resp = requests.get(musician_url).text
        try:
            soup = BeautifulSoup(resp, "lxml").get_text()
        except:
            soup = BeautifulSoup(resp, "html5lib").get_text()

        content = LiveInfo(
                    musician_id=musician_id,
                    content=soup,
                    created_at=date.today())

        session.add(content)

    session.commit()
