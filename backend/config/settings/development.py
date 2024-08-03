from .base import *

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql', #Mysqlの設定
        'NAME': 'app',                        #Mysqlの設定と同じにする以下
        'USER': 'root',
        'PASSWORD':'password',
        'HOST':'host.docker.internal',
        'PORT':'53306',
        'ATOMIC_REQUESTS': True  #HOST,PORTにより53306ポートでMysqlに接続できる
    }
}