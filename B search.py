# 搜索算法优化，正在进行中
# 传入搜索词条
# 返回符合条件的所有树洞（按内容查询）
@app.route('/treeHole/search', methods=['GET'])
def tree_hole_search():
    # req_data = request.get_json()
    text = request.args.get("text")
    try:
        get_holes = db.session.query(TreeHole).filter(
            TreeHole.content.like('%{keyword}%'.format(keyword=text))).all()

        tree_holes = []
        for h in get_holes:
            tree_holes.append(h.to_dict())
        count = len(tree_holes)

        # hole = [h.to_dict() for h in get_holes.items]  # 对每个查询结果转化
        data = {
            "tree_holes": tree_holes,
            "count": count
        }
        return jsonify(code=200, msg="获取成功", data=data)
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="获取失败")
