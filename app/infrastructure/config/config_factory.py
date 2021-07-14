import os
import sys

class BaseConfig():
    ENV = ''

    def __init__(self, env) -> None:
        self.ENV = env

class DevelopmentConfig(BaseConfig):
    DB_HOST = '127.0.0.1'
    DB_NAME = 'banking'
    DB_USER = 'root'
    DB_PASS = 'admin'

class StagingConfig(BaseConfig):
    DB_HOST = '127.0.0.1'
    DB_NAME = 'banking'
    DB_USER = 'root'
    DB_PASS = 'admin'

class ProductionConfig(BaseConfig):
    DB_HOST = '127.0.0.1'
    DB_NAME = 'banking'
    DB_USER = 'root'
    DB_PASS = 'admin'


class ConfigFactory():

    def create(self):
        try: 
            ENV = os.environ.get('ENV')
        except KeyError:
            print('ENV KEYERROR')
            sys.exit(1)
        
        if ENV == None:
            print('Please set the environment variable: ENV')
            sys.exit(1)

        print('\n\n ENV-------',ENV)
        if ENV not in ['development','staging','production']:
            print("The ENV environment variable must be development, staging or production")
            sys.exit(1)
        
        if ENV == 'production':
            return ProductionConfig(ENV)
        elif ENV == 'staging':
            return StagingConfig(ENV)
        else:
            return DevelopmentConfig(ENV)