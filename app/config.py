class Config:
    pass

class DeveloppmentConfig(Config):
  debug = True

config={
    'developpmenet':DeveloppmentConfig,
    'defaul': DeveloppmentConfig

}