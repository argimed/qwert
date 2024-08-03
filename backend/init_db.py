from base import Base, engine, SessionLocal, User

Base.metadata.create_all(bind=engine)

db = SessionLocal()
users = [
    User(login='pavel', email='a@gmail.com', hashed_password='password1'),
    User(login='yura', email='b@gmail.com', hashed_password='password2'),
    User(login='oleg', email='ybwtp@gmail.com', hashed_password='password3'),
]

for user in users:
    db.add(user)

db.commit()

db.close()

print("Database initialized with users.")
