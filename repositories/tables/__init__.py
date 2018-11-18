# -*- encoding:utf-8 -*-

from sqlalchemy import (Column, String, Text, Date, ForeignKey, \
                create_engine, MetaData, DECIMAL, DATETIME, exc, event, Index)
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import (sessionmaker, relationship, scoped_session)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import INTEGER as Integer
from datetime import datetime
import os

USER = "root"
HOST = os.environ['DB_HOSTNAME']
DB = "live_info_crawler"
PW = os.environ['LIVE_INFO_PASSWORD']
DATABASE = f'mysql://{USER}:{PW}@{HOST}/{DB}?charset=utf8'
ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True  # Trueだと実行のたびにSQLが出力される
)

Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))

metadata = MetaData(ENGINE)
Base = declarative_base()


class Musician(Base):
  __tablename__ = 'musicians'

  id = Column(Integer, primary_key=True)
  name = Column(String(255))
  live_info_url = Column(String(255))
  live_info = relationship("LiveInfo")
  updated_live_info = relationship("UpdatedLiveInfo")


class LiveInfo(Base):
  __tablename__ = 'live_info'

  id = Column(Integer, primary_key=True)
  content = Column(Text(4294000000))
  musician_id = Column(Integer, ForeignKey('musicians.id', onupdate='CASCADE', ondelete='CASCADE'))
  created_at = Column(Date)


class UpdatedLiveInfo(Base):
  __tablename__ = 'updated_live_info'

  id = Column(Integer, primary_key=True)
  content = Column(Text(4294000000))
  musician_id = Column(Integer, ForeignKey('musicians.id', onupdate='CASCADE', ondelete='CASCADE'))
  created_at = Column(Date)


if __name__ == "__main__":
    # create table
    Base.metadata.create_all(ENGINE)


# HOW TO DUMP
# mysqldump -u root -h localhost live_info_crawler > mysqldump.sql
