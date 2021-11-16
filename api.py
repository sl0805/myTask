'''
Author: your name
Date: 2021-11-15 16:09:35
LastEditTime: 2021-11-16 20:31:08
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python\1TreeHole\app\api.py
'''
# 各个接口的编写
import flask
from __init__ import db
from models import User, TreeHole, ClickLike, Collect, Comment, Diary, PushMsg
from flask import Flask, request, jsonify, Blueprint, render_template
from flask import abort, redirect, session
from sqlalchemy import extract, and_
app = Flask(__name__)

# 增加日记  我
# 日记表增加
# 前端传来日记内容和标签
@app.route('/diary/addDiary', methods=['POST'])
def addDiary():
    data = request.get_json()
    diaryContent = data.diaryContent
    tips = data.tips
    # 33
    userId = ''

    return

# 删除日记  我
# 日记表删除
@app.route('/diary/deleteDiary', methods=['DELETE'])
def deleteDiary():

    return

# 推送  我
# 推送表查询
# 根据日记标签推送
@app.route('/pushMsg', methods=['GET', 'POST'])
def pushMsg():

    return

# 获取全部日记  我
# 日记表查询
# 根据用户id
@app.route('/diary/getAll', methods=['GET'])
def getAllDiary():

    return

# 根据标签获取日记  我
# 日记表查询
# 根据用户id和标签
@app.route('/diary/getByTips/<tip>', methods=['GET'])
def getDiaryByTips():

    return

# 我的点赞  我
# 点赞表和树洞表查询    根据找到的点赞找到树洞帖子的信息
# 需要知道当前用户
# 返回是否成功信息，同时返回我点赞的所有树洞，后期可看是否按页返回
@app.route('/treeHole/myLike', methods=['POST'])
def getMyLike():

    return

# 我的评论  我
# 评论表和树洞表查询    根据找到的评论找到树洞帖子信息
# 需要知道当前用户
# 返回是否成功信息，同时返回我的所有评论以及其对应树洞（对象数组），后期可看是否按页返回
@app.route('/treeHole/myComment', methods=['POST'])
def getMyComment():

    return


# 树洞提交
# 需要知道当前用户
# 返回是否成功信息
@app.route('/treeHole/write', methods=['POST'])
def writeTreeHole():

    return

# 点赞以及取消点赞
# 需要知道当前用户    传入树洞id号
# 返回是否成功信息以及当前是否点赞
@app.route('/treeHole/GiveALike/<treeHole_id>/', methods=['POST'])
def treeHoleGiveALike():

    return

# 评论
# 需要知道当前用户    传入树洞id号以及评论内容
# 返回是否成功信息，同时返回该树洞的所有评论（对象数组）供前端进行渲染，后期可看是否按页返回
@app.route('/treeHole/addComment/<treeHole_id>/', methods=['POST'])
def treeHoleAddComment():

    return


# 获取树洞
# 传入页数?
# 返回是否成功信息，同时按页返回所有树洞信息（数组）：内容、评论、我是否点赞
@app.route('/treeHole/getAll', methods=['GET'])
def getAllTreeHole():

    return

# 树洞详情页
# 传入树洞id
# 返回是否成功信息，同时返回该树洞的评论、点赞数、我是否点赞
@app.route('/treeHole/detail/<treeHole_id>/', methods=['GET'])
def detail(treeHole_id):

    return

# 树洞内搜索功能
# 传入搜索词条
# 返回符合条件的所有树洞（按内容查询），返回其评论、点赞数以及我是否点赞
@app.route('/treeHole/search', methods=['GET', 'POST'])
def treeHoleSearch():

    return

# 删除树洞
# 传入树洞id
# 返回是否删除成功
@app.route('/treeHole/delete/<treeHole_id>', methods=['DELETE'])
def treeHoleDelete():

    return


if __name__ == '__main__':
    app.run()
