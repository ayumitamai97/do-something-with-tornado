# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from repositories import *
from repositories.tables import *

class LiveInfo(Base):
  """テーブル定義"""
  __tablename__ = 'live_info'

  id = Column(Integer, primary_key=True)
  content = Column(String)
  musician_id = relationship("Musician")
