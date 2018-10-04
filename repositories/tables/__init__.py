# -*- encoding:utf-8 -*-

from sqlalchemy import (Column, String, Text, ForeignKey, \
                create_engine, MetaData, DECIMAL, DATETIME, exc, event, Index)
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import (sessionmaker, relationship, scoped_session)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import INTEGER as Integer
from datetime import datetime


USER = "root"
HOST = "localhost"
DB = "live_info_reader"
DATABASE = f'mysql://{USER}:@{HOST}/{DB}?charset=utf8'
ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True  # Trueだと実行のたびにSQLが出力される
)

Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))

metadata = MetaData(ENGINE)
Base = declarative_base()


class Musician(Base):
  """テーブル定義"""
  __tablename__ = 'musicians'

  id = Column(Integer, primary_key=True)
  name = Column(String(255))
  live_info = relationship("LiveInfo")


class LiveInfo(Base):
  """テーブル定義"""
  __tablename__ = 'live_info'

  id = Column(Integer, primary_key=True)
  content = Column(Text(4294000000))
  musician_id = Column(Integer, ForeignKey('musicians.id', onupdate='CASCADE', ondelete='CASCADE'))


if __name__ == "__main__":
    # create table
    Base.metadata.create_all(ENGINE)
