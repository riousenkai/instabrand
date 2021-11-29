from app.models import db, Comment
from datetime import datetime

# Adds a demo user, you can add other users here if you want
def seed_comments():
    comment1 = Comment(user_id=1, post_id=2, description="I comment on my own posts", createdAt=datetime.now())
    comment2 = Comment(user_id=2, post_id=1, description="Hello!", createdAt=datetime.now())
    comment3 = Comment(user_id=3, post_id=1, description="Woaaah", createdAt=datetime.now())
    comment4 = Comment(user_id=13, post_id=4, description="Go Dolphins instead dude", createdAt=datetime.now())
    comment5 = Comment(user_id=9, post_id=4, description="NO. Bear Down.", createdAt=datetime.now())
    comment6 = Comment(user_id=4, post_id=5, description="NERDDDDDDDD", createdAt=datetime.now())
    comment7 = Comment(user_id=6, post_id=6, description="Can you not? This brings back bad memories.", createdAt=datetime.now())
    comment8 = Comment(user_id=9, post_id=7, description="I'm going next year dude! You going?", createdAt=datetime.now())
    comment9 = Comment(user_id=14, post_id=7, description="Revan! Heck yes!", createdAt=datetime.now())
    comment10 = Comment(user_id=3, post_id=8, description="Looks nice dude", createdAt=datetime.now())
    comment11 = Comment(user_id=4, post_id=9, description="You are a nerd but this looks clean!", createdAt=datetime.now())
    comment12 = Comment(user_id=6, post_id=10, description="No you weren't. Don't lie.", createdAt=datetime.now())
    comment13 = Comment(user_id=9, post_id=10, description="Shhhhhhh....", createdAt=datetime.now())
    comment14 = Comment(user_id=3, post_id=11, description="All good I don't play either", createdAt=datetime.now())
    comment15 = Comment(user_id=12, post_id=11, description="Looking good! Come say hi sometime~", createdAt=datetime.now())
    comment16 = Comment(user_id=10, post_id=12, description="Nerd", createdAt=datetime.now())
    comment17 = Comment(user_id=13, post_id=12, description="What Ann said", createdAt=datetime.now())
    comment18 = Comment(user_id=14, post_id=12, description="What they both said", createdAt=datetime.now())
    comment19 = Comment(user_id=3, post_id=12, description="I think it looks clean", createdAt=datetime.now())
    comment20 = Comment(user_id=9, post_id=12, description="Thanks Neb!", createdAt=datetime.now())
    comment21 = Comment(user_id=3, post_id=12, description="Just kidding you nerd", createdAt=datetime.now())
    comment22 = Comment(user_id=13, post_id=13, description="Perfect picture of you. Just the back", createdAt=datetime.now())
    comment23 = Comment(user_id=14, post_id=13, description="What set was this?", createdAt=datetime.now())
    comment24 = Comment(user_id=9, post_id=13, description="@David - Lost Frequencies! They were so mellow for my taste though", createdAt=datetime.now())
    comment25 = Comment(user_id=9, post_id=14, description="I don't like using her on games.", createdAt=datetime.now())
    comment26 = Comment(user_id=3, post_id=14, description="Takes a bit of time to get used to her", createdAt=datetime.now())
    comment27 = Comment(user_id=9, post_id=15, description="You took forever to watch this. Pretty good though huh?", createdAt=datetime.now())
    comment28 = Comment(user_id=4, post_id=15, description="Mannnn this movie was great!", createdAt=datetime.now())
    comment29 = Comment(user_id=9, post_id=16, description="My name Jeff", createdAt=datetime.now())
    comment30 = Comment(user_id=4, post_id=16, description="Brandon", createdAt=datetime.now())
    comment31 = Comment(user_id=10, post_id=16, description="Ann", createdAt=datetime.now())
    comment32 = Comment(user_id=3, post_id=16, description="Your Name is the anime's name", createdAt=datetime.now())
    comment33 = Comment(user_id=13, post_id=16, description="Andrew", createdAt=datetime.now())
    comment34 = Comment(user_id=14, post_id=16, description="David", createdAt=datetime.now())
    comment35 = Comment(user_id=3, post_id=16, description="Seriously?", createdAt=datetime.now())
    comment36 = Comment(user_id=10, post_id=17, description="This does rock!", createdAt=datetime.now())
    comment37 = Comment(user_id=9, post_id=18, description="Same dude", createdAt=datetime.now())
    comment38 = Comment(user_id=9, post_id=19, description="Do you even lift bro?", createdAt=datetime.now())
    comment39 = Comment(user_id=1, post_id=21, description="I see you...", createdAt=datetime.now())
    comment40 = Comment(user_id=8, post_id=22, description="I have always wanted to go!", createdAt=datetime.now())
    comment41 = Comment(user_id=9, post_id=23, description="I want this!", createdAt=datetime.now())
    comment42 = Comment(user_id=8, post_id=23, description="It's $34.99 at Amazon", createdAt=datetime.now())
    comment43 = Comment(user_id=9, post_id=23, description="Nevermind", createdAt=datetime.now())
    comment44 = Comment(user_id=13, post_id=24, description="Yes?", createdAt=datetime.now())
    comment45 = Comment(user_id=10, post_id=24, description="Yup", createdAt=datetime.now())
    comment46 = Comment(user_id=4, post_id=24, description="This Rocks! -The Rock", createdAt=datetime.now())
    comment47 = Comment(user_id=9, post_id=25, description="WHOOPS", createdAt=datetime.now())
    comment48 = Comment(user_id=9, post_id=26, description="Release a new GTA soon?", createdAt=datetime.now())
    comment49 = Comment(user_id=9, post_id=27, description="I have a girlfriend and you are married... Chill", createdAt=datetime.now())
    comment50 = Comment(user_id=9, post_id=28, description="It's okay you'll win sometime in the future like maybe 2030", createdAt=datetime.now())
    comment51 = Comment(user_id=13, post_id=28, description="You really think so?", createdAt=datetime.now())
    comment52 = Comment(user_id=9, post_id=28, description="Nope", createdAt=datetime.now())
    comment53 = Comment(user_id=4, post_id=29, description="I live so close to you!", createdAt=datetime.now())



    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_comments():
    db.session.execute('TRUNCATE comments RESTART IDENTITY CASCADE;')
    db.session.commit()
