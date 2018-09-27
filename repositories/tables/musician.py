# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, ForeignKey
from repositories import *
from repositories.tables import *

class Musician(Base):
  """テーブル定義"""
  __tablename__ = 'musicians'

  id = Column(Integer, primary_key=True, ForeignKey('musician.id',onupdate='CASCADE', ondelete='CASCADE'))
  name = Column(String)
