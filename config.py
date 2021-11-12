'''
Author: your name
Date: 2021-11-10 15:47:18
LastEditTime: 2021-11-12 18:00:51
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python\teamwork\app\config.py
'''
# import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
DEBUG = True

# SECRET_KEY = os.urandom(24)
'''
HOSTNAME = ''
PORT = ''
DATABASE = ''
USERNAME = ''
PASSWORD = ''
'''
'''
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False
'''
app = Flask(__name__)
app.secret_key = "123456"
# 绑定mysql
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:密码@127.0.0.1:3306/sio'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "jamchaos666"
