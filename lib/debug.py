from models import User
import ipdb
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("sqlite:///user_info.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    
    

ipdb.set_trace()