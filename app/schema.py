from pydantic import BaseModel

class UserInput(BaseModel):
    type: str
    country: str
    listed_in: str
    rating: str