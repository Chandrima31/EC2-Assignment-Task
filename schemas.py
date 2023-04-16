# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 12:17:19 2023

@author: wb578960
"""

from pydantic import BaseModel


class Record(BaseModel):
    PassengerId: int
    Survived: bool
    Pclass: int
    Name: str
    Sex: str
    Age: int
    SibSp: int
    Parch: int
    Ticket: str
    Fare: float
    Cabin: str
    Embarked: str

    class Config:
        orm_mode = True