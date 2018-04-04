import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUT = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')

class ProductionCongig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'data.sqlite')

config = {
    'development' : DevelopmentConfig,
    'production' : ProductionCongig,
    'default' : DevelopmentConfig,
}