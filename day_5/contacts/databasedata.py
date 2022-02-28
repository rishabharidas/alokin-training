from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:password@localhost/test")
connected_engine = engine.connect()