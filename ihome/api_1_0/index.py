# -- coding: utf-8 -- 
# @Author : YBG

from . import api
from ihome import db
import logging

from flask import current_app



@api.route('/index')
def index():

    # logging.error('logss') # 错误级别
    # logging.warning('nj') #警告级别
    # logging.info('ll') # 消息提示级别
    # logging.debug('debug') # 记录调试信息
    current_app.logger.error('error message')
    return 'index page'