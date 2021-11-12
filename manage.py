'''
Author: your name
Date: 2021-11-10 15:47:18
LastEditTime: 2021-11-12 18:05:33
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%A
FilePath: \python\teamwork\manage.py
'''
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from all import app
from exts import db
# from models import
import pymysql
pymysql.install_as_MySQLdb()


manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()
