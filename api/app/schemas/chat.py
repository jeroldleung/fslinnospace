from pydantic import BaseModel


class Chat(BaseModel):
    input: str
