from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    birthday = Column(String, nullable=False)
    country = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username={self.username}, name={self.name}, age={self.age}, country={self.country})>"


class Album(Base):
    __tablename__ = 'albums'

    album_id = Column(Integer, nullable=False, primary_key=True)
    album_name = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    year = Column(Integer, nullable=True)
    rate = Column(Float, nullable=True)
    image_path = Column(String, nullable=True)
    
    def __repr__(self):
        return f"<Album(album_id={self.album_id}, album_name={self.album_name}, artist={self.artist}, year={self.year}, rate={self.rate}, image_path={self.image_path})>"


class Like(Base):
    __tablename__ = 'likes'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    album_id = Column(Integer, ForeignKey('albums.album_id'), primary_key=True)
    like_time = Column(DateTime, nullable=False)