from models import User
from faker import Faker
# import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

fake = Faker()


if __name__ == "__main__":
    engine = create_engine("sqlite:///user_info.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(User).delete()
    
users = [
    User(
        name = fake.name(),
        fullname = fake.name(),
        nickname = fake.name()
    )
    for i in range(50)
]


session.add_all(users)
session.commit()