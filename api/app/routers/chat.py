from fastapi import APIRouter, HTTPException
from openai import InternalServerError, OpenAI
from openai.types.chat import ChatCompletionMessageParam

from app.schemas import Chat

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/")
async def chat_with_model(chat: Chat) -> dict[str, str]:
    client = OpenAI(base_url="http://127.0.0.1:11434/v1", api_key="ollama")
    messages: list[ChatCompletionMessageParam] = [
        {"role": "user", "content": chat.input}
    ]

    try:
        response = client.chat.completions.create(model="llama3.2", messages=messages)
    except InternalServerError:
        e = HTTPException(500, "Failed to generate a chat request from llm services")
        raise e from None

    content = response.choices[0].message.content
    if content is None:
        raise HTTPException(500, "Empty content response from llm services")

    return {"messages": content}
