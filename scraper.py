import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

resp = requests.get("http://www.ivytofraudulentgame.com/live/").text
try:
    soup = BeautifulSoup(resp, "lxml")
except:
    soup = BeautifulSoup(resp, "html5lib")
print(soup.find("body"))

USER = "root"
# PW = os.environ['MYSQL_PW']
HOST = "localhost"
DB = "live_info_reader"
DATABASE = f'mysql://{USER}:{PW}@{HOST}/{DB}?charset=utf8'
ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=config.ENV == 'dev'  # Trueだと実行のたびにSQLが出力される
)

Session = sessionmaker(bind=ENGINE)

session = Session()

