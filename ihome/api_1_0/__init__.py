# -- coding: utf-8 -- 
# @Author : YBG


from  flask import Blueprint
# 蓝图参数   1 蓝图名字  2 __name__
api = Blueprint('api_1_0',__name__)

from . import index