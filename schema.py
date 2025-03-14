from pydantic import BaseModel
from typing import Optional, Union
from typing import Optional


class GetTopicRequest(BaseModel):
    user_id: str
    class_level: str
    board:str
    subject:str
    topic:str

class GetAnswerRequest(BaseModel):
    user_id: str
    class_level: str
    board:str
    subject:str
    question:str

class GetTopicResponse(BaseModel):
    response:str
    questions:list[str]

class GetAnswerResponse(BaseModel):
    answer:str
