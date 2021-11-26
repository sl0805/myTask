@app.route('/treeHole/search', methods=['GET'])
def tree_hole_search():
    text = request.args.get("text")
    # 关键词分开
    keyword_arr = text.split(' ')
    # 消除空格
    text = text.replace(" ", '')
    try:
        rule = or_(*[TreeHole.content.like('%'+keyword+'%')
                     for keyword in text])
        get_holes = db.session.query(TreeHole).filter(rule).all()
        # get_holes = db.session.query(TreeHole).filter(TreeHole.content.op('%s'%text1)(REGEX))
        tree_holes = []
        for h in get_holes:
            h1 = h.to_dict()
            a = 0
            for k in keyword_arr:
                a += fuzz.partial_ratio(k, h.content)
            h1['order'] = a
            tree_holes.append(h1)

        tree_holes = sorted(tree_holes, key=lambda r: r['order'], reverse=True)
        count = len(tree_holes)
        data = {
            "tree_holes": tree_holes,
            "count": count
        }
        return jsonify(code=200, msg="获取成功", data=data)
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="获取失败")
