from fastapi import FastAPI

from app.routers import chat

app = FastAPI(
    title="fslinnospace-api", swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)

app.include_router(chat.router)
