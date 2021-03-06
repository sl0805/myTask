'''
Author: your name
Date: 2021-11-10 15:47:18
LastEditTime: 2021-11-10 16:20:42
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python\teamwork\models.py
'''
from exts import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    avatar = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)


class treeHole(db.Model):
    __tablename__ = 'treeHole'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    pic_filename = db.Column(db.String(100), nullable=False)
    video_filename = db.Column(db.String(100), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref=db.backref('video'))
    thumb_num = db.Column(db.Integer, nullable=False)
    collect_num = db.Column(db.Integer, nullable=False)
    tip = db.Column(db.String(100), nullable=False)


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_time = db.Column(db.DateTime, default=datetime.now)
    video = db.relationship('Video', backref=db.backref(
        'comment', order_by=id.desc()))
    author = db.relationship('User', backref=db.backref('comment'))


class Like(db.Model):
    __tablename__ = 'like'
    # 被收藏的视频、收藏的用户是谁
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    video = db.relationship('Video', backref=db.backref('collect'))
    author = db.relationship('User', backref=db.backref('collect'))
