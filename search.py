@app.route('/treeHole/search', methods=['GET'])
def tree_hole_search():
    # req_data = request.get_json()
    text = request.args.get("text")
    pattern = map(lambda k: "(?=.*%s)" % k, text.split(" "))
    # findall是找到所有的字符,再在字符中添加空格，当然你想添加其他东西当然也可以
    text1 = '%'.join(pattern)
    try:
        get_holes = db.session.query(TreeHole).filter(
            TreeHole.content.like('%{keyword}%'.format(keyword=text1))).all()

        tree_holes = []
        for h in get_holes:
            h1 = h.to_dict()
            a = fuzz.partial_ratio(text, h.content)
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
