#!/usr/bin/env python

import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import PasswordType, EmailType

from constants import Constants

from db import session

Base = declarative_base()
Base.query = session.query_property()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    email = Column(EmailType(length=128))
    password = Column(PasswordType(schemes=['pbkdf2_sha512', 'md5_crypt'], deprecated=['md5_crypt']))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, unique=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    # TODO: Create a separate reactions table
    image_name = Column(String(128), nullable=False)

    content = Column(String(512), nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    is_liked = Column(TINYINT(unsigned=True), default=Constants.POST_NOT_LIKED)

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from config import SQLALCHEMY_DATABASE_URI
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)