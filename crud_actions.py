from datetime import datetime

from mapping import Album, Like, User 
from sqlalchemy import desc, func


def add_user(session, username, password, name, birthday, country):
    user = User(username=username, password=password, name=name, birthday=birthday, country=country)
    session.add(user)
    session.commit()
    return user


def update_user(session, user_id, username, name, birthday, country):
    user = get_user_by_id(session, user_id)
    user.username = username
    user.name = name
    user.birthday = birthday
    user.country = country
    session.commit()
    return user


def get_user_by_username(session, username):
    return session.query(User).filter(User.username == username).first()


def get_user_by_id(session, user_id):
    return session.query(User).filter(User.user_id == user_id).first()


def get_album_by_album_id(session, album_id):
    return session.query(Album).filter(Album.album_id == album_id).first()


def add_or_update_album(session, album_id, album_name, artist, year, rate, image_path):
    existing_album = get_album_by_album_id(session, album_id)
    if existing_album is None:
        album = Album(
            album_id=album_id, album_name=album_name, artist=artist, year=year, rate=rate, image_path=image_path)
        session.add(album)
    else:
        existing_album.rate = rate
        existing_album.image_path = image_path 
    session.commit()


def add_like_by_ids(session, user_id, album_id):
    like = Like(user_id=user_id, album_id=album_id, like_time=datetime.now())
    session.add(like)
    session.commit()


def get_like_data(session, user_id, album_id):
    return (
        session.query(Like).filter(Like.album_id == album_id)
        .filter(Like.user_id == user_id).first()
    )


def delete_like(session, user_id, album_id):
    like = get_like_data(session, user_id, album_id)
    session.delete(like)
    session.commit()


def get_likes_albums_by_user_id(session, user_id):
    return (
        session.query(Album).join(Like).join(User)
        .filter(User.user_id == user_id)
        .order_by(desc(Like.like_time)).all()
    )


def get_likes_per_user(session, user_id):
    return session.query(Like).filter(Like.user_id == user_id).count()
 

def get_album_likes_amount(session, album_id):
    rows_num = session.query(Like).filter(Like.album_id == album_id).count()
    return rows_num


def get_top_likes_albums(session):
    return (
        session.query(Album, func.count(Like.user_id))
        .join(Like).group_by(Album)
        .order_by(desc(func.count(Like.user_id)))[:10]
    )

