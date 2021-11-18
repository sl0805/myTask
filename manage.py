class TreeHole(db.Model):
    __tablename__ = "TreeHole"  # 设置表名
    tree_hole_id = db.Column(db.String(50), primary_key=True)  # 帖id
    user_id = db.Column(db.String(50), nullable=False, index=True)  # 用户id
    # 帖内容!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    content = db.Column(db.String(2000), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.now)  # 时间
    likes = db.Column(db.Integer, default=0)  # 点赞数
    comments = db.Column(db.Integer, default=0)  # 评论数
    collects = db.Column(db.Integer, default=0)  # 点赞数

    def to_dict(self):
        data = {
            'tree_hole_id': self.tree_hole_id,
            'user_id': self.user_id,
            'content': self.content,
            'time': self.time,
            'likes': self.likes,
            'comments': self.comments,
            'collects': self.collects,
            # 'comments': url_for('get_comment_json', article_id=self.id),  # 这里返回一个路由
            # 'new_comment': {'comments': self.filter_c}  # 创建过滤函数，查询所有评论
        }
        return data


class ClickLike(db.Model):
    __tablename__ = "ClickLike"  # 设置表名
    tree_hole_id = db.Column(
        db.String(50), primary_key=True, index=True)  # 帖id
    user_id = db.Column(db.String(50), primary_key=True, index=True)  # 用户id
    time = db.Column(db.DateTime, nullable=False, default=datetime.now)  # 时间

    def to_dict(self):
        data = {
            'tree_hole_id': self.tree_hole_id,
            'user_id': self.user_id,
            'time': self.time
        }
        return data


class Collect(db.Model):
    __tablename__ = "Collect"  # 设置表名
    tree_hole_id = db.Column(db.String(50), primary_key=True)  # 帖id
    user_id = db.Column(db.String(50), primary_key=True, index=True)  # 用户id
    time = db.Column(db.DateTime, nullable=False, default=datetime.now)  # 时间

    def to_dict(self):
        data = {
            'tree_hole_id': self.tree_hole_id,
            'user_id': self.user_id,
            'time': self.time
        }
        return data


class Comment(db.Model):
    __tablename__ = "Comment"  # 设置表名
    comment_id = db.Column(db.String(50), primary_key=True)  # 评论id
    # parentCommentId = db.Column(db.String(50), primary_key=True)  # 父评论id
    tree_hole_id = db.Column(db.String(50), primary_key=True)  # 帖id
    user_id = db.Column(db.String(50), index=True)  # 用户id
    # 评论内容!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    comment_content = db.Column(db.String(2000), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.now)  # 时间

    def to_dict(self):
        data = {
            'tree_hole_id': self.tree_hole_id,
            'user_id': self.user_id,
            'comment_id': self.comment_id,
            'comment_content': self.comment_content,
            'time': self.time
        }
        return data


class Diary(db.Model):
    __tablename__ = "Diary"  # 设置表名
    # diary_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 日记id
    diary_id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), nullable=False, index=True)  # 用户id
    tips = db.Column(db.String(5000), nullable=False)
    diary_content = db.Column(db.String(5000), nullable=False)  # 日记内容
    write_down_time = db.Column(db.DateTime, default=datetime.now)  # 记录日期

    '''__mapper_args__ = {
         "order_by": write_down_time.desc()
    }'''

    def to_dict(self):
        data = {
            'diary_id': self.diary_id,
            'user_id': self.user_id,
            'tips': self.tips,
            'diary_content': self.diary_content,
            'write_down_time': self.write_down_time
        }
        return data


class PushMsg(db.Model):
    __tablename__ = "PushMsg"
    pushmsg_id = db.Column(db.String(50), primary_key=True)  # 推送id
    # 推送内容!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
    content = db.Column(db.String(5000), nullable=False)
    # 推送标签!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    tips = db.Column(db.String(50))

    def to_dict(self):
        data = {
            'pushmsg_id': self.pushmsg_id,
            'content': self.content,
            'tips': self.tips
        }
        return data


# 新建日记
@app.route('/diary/addDiary/', methods=['POST'])
def add_diary():
    data = request.get_json()
    diary_content = data.get('diary_content')
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!openid全局变量的获取
    user_id = data.get('user_id')
    # 获取当前时间并转成字符串
    # time = datetime.strptime
    tips = data.get('tips')
    # time = data.get('time')
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    diary_id = user_id+time
    try:
        diary = Diary(diary_id=diary_id, user_id=user_id, tips=tips,
                      diary_content=diary_content)
        db.session.add(diary)
        db.session.commit()
        return jsonify(code=200, msg="日记保存成功")
    except:
        # print(e)
        db.session.rollback()
        return jsonify(code=400, msg="保存失败")
# 删除日记  我
# 日记表删除
# 前端传来日记id
@app.route('/diary/deleteDiary/', methods=['POST'])
def delete_diary():
    data = request.get_json()
    diary_id = data.get('diary_id')
    get_diary = Diary.query.filter(Diary.diary_id == diary_id).all()
    find_diary = []  # [p.to_dict() for p in get_pushMsg]
    for p in get_diary:
        find_diary.append(p.to_dict())
    data = {"find_diary": find_diary}
    count = len(find_diary)
    if count != 0:  # 是否有数据
        # 增加未找到的情况！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！1
        #
        try:
            Diary.query.filter(Diary.diary_id == diary_id).delete()
            db.session.commit()
            msg = "删除成功"
            return jsonify(code=200, msg=msg, data=data)
        except:
            db.session.rollback()
            return jsonify(code=400, msg="删除失败")
    else:
        msg = "日记不存在"
        return jsonify(code=200, msg=msg)

        # 增加未找到的情况！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！1
    # Diary.query.filter(Diary.diary_id==diary_id).delete()
    # db.session.commit()
    # return jsonify(code=200, msg="删除成功",data=data)
        # return diary

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!未完成
# 推送  我
# 推送表查询
# 前端传来日记标签
@app.route('/pushMsg', methods=['POST'])
def push_msg():
    data = request.get_json()
    diary_tip = data.get('diary_tip')

    try:
        get_pushMsg = PushMsg.query.filter(PushMsg.tips == diary_tip).all()
        pushMsg = []  # [p.to_dict() for p in get_pushMsg]
        for p in get_pushMsg:
            pushMsg.append(p.to_dict())
        count = len(pushMsg)
        data = {
            "pushMsg": pushMsg
        }
        if count:
            num = random.randint(0, count-1)
            get_one = pushMsg[num]  #
            return jsonify(code=200, msg="获取成功", data=get_one)
        else:
            return jsonify(code=200, msg="没有相关推送")
    except:
        return jsonify(code=400, msg="推送失败")


# 获取全部日记  我
# 日记表查询
# 前端传入页数和页总量
@app.route('/diary/getAll', methods=['GET'])
def get_all_diary():
    data = request.get_json()
    page = data.get('page')
    per_page = data.get('per_page')
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111
    user_id = data.get('user_id')
    try:
        # 分页：第一个参数表示页数，第二个参数表示每页条目数，第三个参数分页异常不报错
        get_per_page = Diary.query.filter(Diary.user_id == user_id).order_by(Diary.write_down_time.desc()).paginate(
            page, per_page, False)
        # objects = db.session.query(Protocols).filter_by(is_default=0).order_by(sqlalchemy.func.field(Protocols.parent_protocol, "ip", "udp", "tcp"))

        diary_arr = get_per_page.items  # 获取分页后的数据
        page_num = get_per_page.pages  # 获取分页后的总页数
        curpage = get_per_page.page  # 获取当前页数
        all_diary = []
        for p in diary_arr:
            all_diary.append(p.to_dict())
        page_count = len(all_diary)
        # return jsonify(code=200, msg="查询成功", page_num=page_num, curpage=curpage, data=diary_arr)
        if page_count > 0:
            return jsonify(code=200, msg="查询成功", page_num=page_num, curpage=curpage, page_count=page_count, all_diary=all_diary)
        else:
            return jsonify(code=200, msg="没有数据")
    except:
        return jsonify(code=400, msg="查询失败")

# 根据标签获取日记  我
# 日记表查询
# 前端传入标签、页数、页容量
@app.route('/diary/getByTips', methods=['GET'])
def get_diary_by_tips():
    data = request.get_json()
    tips = data.get('tips')
    page = data.get('page')
    per_page = data.get('per_page')
    user_id = data.get('user_id')

    try:
        # 分页：第一个参数表示页数，第二个参数表示每页条目数，第三个参数分页异常不报错
        get_per_page = Diary.query.filter(Diary.tips == tips, Diary.user_id == user_id).order_by(Diary.write_down_time.desc()).paginate(
            page, per_page, False)
        diary_arr = get_per_page.items  # 获取分页后的数据
        page_num = get_per_page.pages  # 获取分页后的总页数
        curpage = get_per_page.page  # 获取当前页数

        all_diary = []
        for p in diary_arr:
            all_diary.append(p.to_dict())
        page_count = len(all_diary)
        # return jsonify(code=200, msg="查询成功", page_num=page_num, curpage=curpage, data=diary_arr)
        if page_count > 0:
            return jsonify(code=200, msg="查询成功", page_num=page_num, curpage=curpage, page_count=page_count, all_diary=all_diary)
        else:
            return jsonify(code=200, msg="没有数据")
    except:
        return jsonify(code=400, msg="查询失败")

# 我的点赞  我
# 点赞表和树洞表查询    根据找到的点赞找到树洞帖子的信息
# 前端需传入user_id
# 返回是否成功信息，同时返回我点赞的所有树洞，后期可看是否按页返回
@app.route('/treeHole/myLike', methods=['GET'])
def get_my_like():
    data = request.get_json()
    # ！！！！！！！！！！！！！！！！！！！！！
    user_id = data.get('user_id')
    # 先从点赞表中获取我点赞的所有树洞id
    get_all_treeHole = ClickLike.query.filter(
        ClickLike.user_id == user_id).order_by(ClickLike.time.desc()).all()
    my_like = []
    for item in get_all_treeHole:
        my_like.append(item.to_dict())
    count = len(my_like)
    # 通过树洞id去树洞表中找，并将其放进
    return jsonify(code=200, msg="查询成功", data=my_like)


# 我的评论  我
# 评论表和树洞表查询    根据找到的评论找到树洞帖子信息
# 前端不用穿任何数据
# 返回是否成功信息，同时返回我的所有评论总数以及其对应树洞id
@app.route('/treeHole/myComment', methods=['GET'])
def get_my_comment():
    data = request.get_json()
    # ！！！！！！！！！！！！！！！！！！！！！
    user_id = data.get('user_id')
    # 先从评论表中获取我所有评论的
    get_comment = Comment.query.filter(
        Comment.user_id == user_id).order_by(Comment.time.desc()).all()
    my_comment = []
    for c in get_comment:
        # 评论的内容 评论的树洞id获取
        my_comment.append(c.to_dict())
    count = len(my_comment)
    # 通过树洞id去树洞表中找，并将其放进
    return jsonify(code=200, msg="查询成功", data=my_comment, count=count)


# 我的收藏
# 收藏表和树洞表查询    根据找到的收藏找到树洞帖子的信息
# 前端无需传入任何数据
# 返回是否成功信息，同时返回我收藏的所有树洞，后期可看是否按页返回
@app.route('/treeHole/mycollect', methods=['GET'])
def get_my_collect():
    data = request.get_json()
    user_id = data.get('user_id')
    # 先从收藏表中获取我收藏的所有树洞id
    get_all_treeHole = Collect.query.filter(
        Collect.user_id == user_id).order_by(Collect.time.desc()).all()
    my_collect = []
    for item in get_all_treeHole:
        my_collect.append(item.to_dict())
    count = len(my_collect)
    return jsonify(code=200, msg="查询成功", data=my_collect, count=count)
