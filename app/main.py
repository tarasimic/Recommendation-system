from fastapi import FastAPI
from app.api import router as user_input

app = FastAPI()

app.include_router(user_input)