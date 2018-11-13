from flask import Flask

from myapp.ext import init_ext
from myapp.settings import conf
from myapp.views import init_blue


def create_app(env_name):
    #做校验
    if not env_name in conf.keys():
        raise Exception('您的环境名有问题')
    app = Flask(__name__)

    #配置
    app.config.from_object(conf.get(env_name))
    #注册各种第三方插件
    init_ext(app)
    #注册蓝图
    init_blue(app)

    return app