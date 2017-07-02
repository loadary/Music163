#!/usr/bin/env python
# coding:utf-8

from config import DATABASE
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()    # 元类

class Comment(Base):
    """
    评论列表
    """
    __tablename__ = '163_comment'

    id = Column(Integer, primary_key=True)
    userId = Column(Integer)                    # 用户id
    nickname = Column(String(length=200))       # 名称
    avatarUrl = Column(String(length=200))      # 头像地址
    content = Column(Text, unique=True)                      # 评论内容
    likedCount = Column(Integer)                # 喜欢数量
    time = Column(DateTime)                     # 创建时间
    song_id = Column(Integer)                   # 歌曲id



engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)s/%(db)s?charset=utf8'%DATABASE, echo=True)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
