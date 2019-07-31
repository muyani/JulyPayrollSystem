class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@127.0.0.1:5432/july_payroll'
    environment = 'Development'
    DEBUG = True

class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@127.0.0.1:5432/july_payroll'
    environment = 'Development'
    DEBUG = True

class Testing(Config):
    DEBUG = False

class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1sggdsgdvshdvhsgdghsg@192.168.10.1:5432/july_payroll'
    DEBUG = False
    environment = 'Production'



