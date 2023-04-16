# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 11:55:31 2023

@author: wb578960
"""

from sqlalchemy import Column, Integer, String, Boolean, Float
from database import Base


class Record(Base):
    __tablename__ = "titanic_data"

    PassengerId = Column(Integer, primary_key=True, index=True)
    Survived = Column(Boolean)
    Pclass = Column(Integer)
    Name = Column(String)
    Sex = Column(String(length=10))
    Age = Column(Integer)
    SibSp = Column(Integer)
    Parch = Column(Integer)
    Ticket = Column(String)
    Fare = Column(Float)
    Cabin = Column(String)
    Embarked = Column(String(length=1))
    