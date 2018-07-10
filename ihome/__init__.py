# -- coding: utf-8 -- 
# @Author : YBG
import redis
import logging
from flask import Flask
from config import config_dict
from  flask_session import Session
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler

# 构建数据库对象  延迟构建
db = SQLAlchemy()
# 构建redis对象
redis_store = None
csrf = CSRFProtect()



# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)  # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日记录器
logging.getLogger().addHandler(file_log_handler)

# 工厂模式
def create_app(config_name):
    app = Flask(__name__)
    conf = config_dict[config_name]
    app.config.from_object(conf)


   # 初始化数据库
    db.init_app(app)
    # 初始化redis
    global redis_store
    redis_store = redis.StrictRedis(host=conf.REDIS_HOST, port=conf.REDIS_PORT)
    # 初始化csrf
    # 创建链接
    # 补充对应的csrf防护机制  仅仅完成了验证操作  从cookie中提取
    # csrf_token字段从body中题=提取csrf_token字段
    # 如果两个值相同，通过验证，进入视图函数执行，如果不同，验证失败
    # 会返回HTTP中的400错误
    csrf.init_app(app)
    # 将 flask里的session保存到redis中
    Session(app)
    import api_1_0
    # 注册蓝图

    app.register_blueprint(api_1_0.api, url_prefix='/api/v1_0')
    return app