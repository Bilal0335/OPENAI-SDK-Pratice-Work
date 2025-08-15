

# ! my_data_type/math_data.py
from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class MyData:
    n1:int
    n2:int
    result:int
    
class CalendarEvent(BaseModel):
    name:str
    date:str
    participants:list[str]
    
class WeatherReport(BaseModel):
    city:str
    temperature:float
    condition:str
    
class BookInfo(BaseModel):
    title:str
    author:str
    year:int
    genres:list[str]
    
    
class UserData(BaseModel):
    name:str
    age:int
    role:str
    
class MyToolSchema(BaseModel):
    n1:int
    n2:int
    
# 1. Input data model
class MyhandoffData(BaseModel):
    reason:str
    result:str
    
    
# -------------------------------
# 1️⃣ Handoff Input Models
# -------------------------------

class MathData(BaseModel):
    reason: str
    value: str

class EnglishData(BaseModel):
    text: str
    reason: str
    
# ! guardrails
class Hoteldata(BaseModel):
    resaon:str
    is_hotel_sannata_query:bool
    is_hotel_sannata_account_or_tax_query:bool