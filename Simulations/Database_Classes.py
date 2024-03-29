from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
Base = declarative_base()

#Environmental Data

#Body Data
class Body_temperature(Base):
    __tablename__ = 'Body_temperature'
    TimeStamp = Column(DateTime, primary_key=True)
    temperature = Column(Float)
    def to_dict(self):
        return {
            'TimeStamp': self.TimeStamp.strftime('%Y-%m-%dT%H:%M:%S'),
            'Temperature': self.temperature
        }

class Heart_Rate(Base):
    __tablename__ = 'Heart_Rate'
    TimeStamp = Column(DateTime, primary_key=True)
    HeartRate = Column(Integer)
    def to_dict(self):
        return {
            'TimeStamp': self.TimeStamp.strftime('%Y-%m-%dT%H:%M:%S'),
            'HeartRate': self.HeartRate
        }

class Blood_Pressure(Base):
    __tablename__ = 'Blood_Pressure'
    TimeStamp = Column(DateTime, primary_key=True)
    Systolic = Column(Integer)
    Diastolic = Column(Integer)
    def to_dict(self):
        return {
            'TimeStamp': self.TimeStamp.strftime('%Y-%m-%dT%H:%M:%S'),
            'Systolic': self.Systolic,
            'Diastolic': self.Diastolic
        }

class Blood_Oxygen(Base):
    __tablename__ = 'Blood_Oxygen'
    TimeStamp = Column(DateTime, primary_key=True)
    Oxygen = Column(Integer)
    def to_dict(self):
        return {
            'TimeStamp': self.TimeStamp.strftime('%Y-%m-%dT%H:%M:%S'),
            'Oxygen': self.Oxygen
        }

class Respiratory_Rate(Base):
    __tablename__ = 'Respiratory_Rate'
    TimeStamp = Column(DateTime, primary_key=True)
    RespiratoryRate = Column(Integer)
    def to_dict(self):
        return {
            'TimeStamp': self.TimeStamp.strftime('%Y-%m-%dT%H:%M:%S'),
            'RespiratoryRate': self.RespiratoryRate
        }

class Sweat(Base):
    __tablename__ = 'sweat'
    TimeStamp = Column(DateTime, primary_key=True)
    Sweat = Column(Integer)
    def to_dict(self):
        return {
            'TimeStamp': self.TimeStamp.strftime('%Y-%m-%dT%H:%M:%S'),
            'Sweat': self.Sweat
        }

class Sugar(Base):
    __tablename__ = 'sugar'
    TimeStamp = Column(DateTime, primary_key=True)
    Sugar = Column(Integer)
    def to_dict(self):
        return {
            'TimeStamp': self.TimeStamp.strftime('%Y-%m-%dT%H:%M:%S'),
            'Sugar': self.Sugar
        }

#Activity Data
class Steps(Base):
    __tablename__ = 'Steps'
    TimeStamp = Column(DateTime, primary_key=True)
    Steps = Column(String)
    def to_dict(self):
        return {
            'TimeStamp': self.TimeStamp.strftime('%Y-%m-%dT%H:%M:%S'),
            'Steps': self.Steps
        }

#Emotional Data
class Emotion(Base):
    __tablename__ = 'Emotion'
    TimeStamp = Column(DateTime, primary_key=True)
    Emotion = Column(String)
    def to_dict(self):
        return {
            'TimeStamp': self.TimeStamp.strftime('%Y-%m-%dT%H:%M:%S'),
            'Emotion': self.Emotion
        }

class Stress(Base):
    __tablename__ = 'Stress'
    TimeStamp = Column(DateTime, primary_key=True)
    Stress = Column(Integer)
    def to_dict(self):
        return {
            'TimeStamp': self.TimeStamp.strftime('%Y-%m-%dT%H:%M:%S'),
            'Stress': self.Stress
        }

