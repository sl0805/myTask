'''
Author: your name
Date: 2020-02-15 13:59:53
LastEditTime: 2021-11-10 20:10:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\sl\decorators.py
'''
from functools import wraps
from flask import session, redirect, url_for

# 类似用来设置用户token


def login_required(func):
    '''@wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper'''
