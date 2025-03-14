from llm import get_llm_response
from logger import logger
from schema import GetAnswerResponse

async def get_answer_service(question: str, class_level: str, board: str, subject: str):
    prompt = open("prompt/get_answer.txt", "r").read()
    prompt = prompt.format(question=question, class_level=class_level, board=board, subject=subject)
    logger.info(f"Prompt: {prompt}")
    response = await get_llm_response(prompt)   
    answer = GetAnswerResponse(answer=response)
    return answer