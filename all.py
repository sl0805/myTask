from flask import Flask, render_template, request, redirect, url_for, session
import config
from models import User, treeHole, Comment, Like
from exts import db
from decorators import login_required
import pymysql

pymysql.install_as_MySQLdb()


app = Flask(__name__)

app.config.from_object(config)
db.init_app(app)


# 树洞提交
# 需要知道当前用户
# 返回是否成功信息
@app.route('/treeHole/write', methods=['POST'])
@login_required
def writeTreeHole():

    return

# 点赞以及取消点赞
# 需要知道当前用户    传入树洞id号
# 返回是否成功信息以及当前是否点赞
@app.route('/treeHole/GiveALike/<treeHole_id>/', methods=['POST'])
@login_required
def treeHoleGiveALike():

    return

# 评论
# 需要知道当前用户    传入树洞id号以及评论内容
# 返回是否成功信息，同时返回该树洞的所有评论（对象数组）供前端进行渲染，后期可看是否按页返回
@app.route('/treeHole/addComment/<treeHole_id>/', methods=['POST'])
@login_required
def treeHoleAddComment():

    return


# 我的点赞
# 需要知道当前用户
# 返回是否成功信息，同时返回我点赞的所有树洞，后期可看是否按页返回
@app.route('/treeHole/myLike', methods=['POST'])
@login_required
def getMyLike():

    return

# 我的评论
# 需要知道当前用户
# 返回是否成功信息，同时返回我的所有评论以及其对应树洞（对象数组），后期可看是否按页返回
@app.route('/treeHole/myComment', methods=['POST'])
@login_required
def getMyComment():

    return

# 获取树洞
# 传入页数
# 返回是否成功信息，同时按页返回所有树洞信息（数组）：内容、评论、我是否点赞
@app.route('/treeHole/getAll', methods=['GET'])
def getAllTreeHole():

    return

# 树洞详情页
# 传入树洞id
# 返回是否成功信息，同时返回该树洞的评论、点赞数、我是否点赞
@app.route('/treeHole/detail/<treeHole_id>/', methods=['GET'])
def detail(treeHole_id):
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    user_role = 'pup'
    if user:
        user_role = user.role
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 2))
    treeHole = treeHole.query.filter(treeHole.id == treeHole_id).first()
    paginate = Comment.query.filter(Comment.treeHole_id == treeHole_id).order_by(
        db.desc(Comment.create_time)).paginate(page, per_page, error_out=False)
    comments = paginate.items
    return

# 树洞内搜索功能
# 传入搜索词条
# 返回符合条件的所有树洞（按内容查询），返回其评论、点赞数以及我是否点赞
@app.route('/treeHole/search', methods=['GET', 'POST'])
def treeHoleSearch():

    return

# 删除
# 传入树洞id
# 返回是否删除成功
@app.route('/treeHole/delete/<treeHole_id>', methods=['DELETE'])
def treeHoleDelete():

    return


@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return{'user': user}
    return {}


if __name__ == '__main__':
    app.run()
