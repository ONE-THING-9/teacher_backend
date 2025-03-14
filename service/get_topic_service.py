from llm import get_llm_response
from logger import logger
import ast
from schema import GetTopicResponse

def post_process_response(response: str):
    questions = ast.literal_eval(response)['questions']
    questions = [question["question"] for question in questions]
    return questions



async def get_topic_service(topic: str, class_level: str, board: str, subject: str):
    prompt = open("prompt/get_topic.txt", "r").read()
    prompt = prompt.format(topic=topic, class_level=class_level, board=board, subject=subject)
    logger.info(f"Prompt: {prompt}")
    response = await get_llm_response(prompt)
    question_prompt = open("prompt/get_question.txt", "r").read()
    question_prompt = question_prompt.format(topic=topic, class_level=class_level, board=board, subject=subject)
    questions = await get_llm_response(question_prompt, grounding=True)
    logger.info(f"Response: {questions}")
    questions = post_process_response(questions)
    response = GetTopicResponse(response=response, questions=questions)
    return response



