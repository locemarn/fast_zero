"""Schemas"""
from pydantic import BaseModel

class Message(BaseModel):
    """message model"""
    message: str
