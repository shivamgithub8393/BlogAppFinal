from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base



engine = create_engine(
    'mysql+pymysql://root:Shivam123@localhost:3306/blogapp')
Base = automap_base()
Base.prepare(engine, reflect = True)


User = Base.classes.users