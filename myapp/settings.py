from redis import StrictRedis

def get_db_uri(conf):
    uri = '{backend}+{engine}://{user}:{pwd}@{ip}:{port}//{db}'.format(
        backend =conf.get('backend'),
        engine =conf.get('engine'),
        user =conf.get('user'),
        pwd =conf.get('pwd'),
        ip =conf.get('ip'),
        port =conf.get('port'),
        db =conf.get('db'),
    )
    return uri

class Config:
    #公共的配置
    Debug = False
    Test = False
    Online = False
    SECRET_KEY= 'guanfangyidiande'
    SESSION_TYPE = 'redis'
    SESSION_KEY_PREFIX = 'myapp:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DebugConfig(Config):
    Debug = True
    SESSION_REDIS = StrictRedis(host = '127.0.0.1',db=5)
    DATABASE = {
        'engine':'pymysql',
        'backend':'mysql',
        'user':'hz1805',
        'pwd':'123456',
        'host':'127.0.0.1',
        'post':'3306',
        'db':'flaskday02'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

class TestConfig(Config):
    Test = True
    SESSION_REDIS = StrictRedis(host='127.0.0.1', db=6)
    DATABASE = {
        'engine': 'pymysql',
        'backend': 'mysql',
        'user': 'hz1805',
        'pwd': '123456',
        'host': '127.0.0.1',
        'post': '3306',
        'db': 'flaskday02-1'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class OnlineConfig(Config):
    Online = True
    SESSION_REDIS = StrictRedis(host='127.0.0.1', db=7)
    DATABASE = {
        'engine': 'pymysql',
        'backend': 'mysql',
        'user': 'hz1805',
        'pwd': '123456',
        'host': '127.0.0.1',
        'post': '3306',
        'db': 'flaskday02-2'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

conf = {
    'debug':DebugConfig,
    'test':TestConfig,
    'online':OnlineConfig
}


