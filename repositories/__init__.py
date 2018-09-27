# -*- coding: utf-8 -*-

import os
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import *

from . import *
from tables import *

Base = declarative_base()

USER = "root"
# PW = os.environ['MYSQL_PW']
HOST = "localhost"
DB = "live_info_reader"
DATABASE = f'mysql://{USER}:@{HOST}/{DB}?charset=utf8'
ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True  # Trueだと実行のたびにSQLが出力される
)

Base.metadata.create_all(bind=ENGINE, checkfirst=False)
