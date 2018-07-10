# -- coding: utf-8 -- 
# @Author : YBG

from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate

from ihome import create_app,db

# 创建flask的app
app = create_app('develop')

# 创建对应的管理工具对象
manger = Manager(app)
Migrate(app,db)
manger.add_command('db', MigrateCommand)





if __name__ == '__main__':
    manger.run()