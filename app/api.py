from fastapi import APIRouter
from app.schema import UserInput
from app.data import encode_input, calculate_similarity, encoded_data, data

router = APIRouter()

@router.post('/')
def user_input(user_input: UserInput):
    user_encoded = encode_input(user_input)
    similarities = calculate_similarity(user_encoded, encoded_data)
    top_indices = similarities[0].argsort()[-5:][::-1]
    top_items = data.iloc[top_indices].to_dict(orient='records')
    return {"similar_items\n": top_items}


    
