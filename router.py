from fastapi import APIRouter
from service.get_topic_service import get_topic_service
from schema import GetTopicRequest
from service.get_answer import get_answer_service
from schema import GetAnswerRequest
router = APIRouter()

from logger import logger

# Add new schema classes for authentication

@router.post("/get_topic")
async def get_topic(get_topic_request: GetTopicRequest):
    response = await get_topic_service(get_topic_request.topic, get_topic_request.class_level, get_topic_request.board, get_topic_request.subject)
    return response

@router.post("/get_answer")
async def get_answer(get_answer_request: GetAnswerRequest):
    response = await get_answer_service(get_answer_request.question, get_answer_request.class_level, get_answer_request.board, get_answer_request.subject)
    return response

