import pandas as pd
from typing import List
from app.schema import UserInput
from sklearn.metrics.pairwise import cosine_similarity


data = pd.read_csv('netflix_titles.csv')

data = data.drop_duplicates()

CATEGORICAL_COLUMNS = ['type', 'country', 'listed_in', 'rating']
encoded_data = pd.get_dummies(data[CATEGORICAL_COLUMNS])



def encode_input(user_input: UserInput):
    user_input_dict = user_input.model_dump()
    user_input_df = pd.DataFrame([user_input_dict])
    encoded_user = pd.get_dummies(user_input_df, columns=CATEGORICAL_COLUMNS)
    encoded_user = encoded_user.reindex(columns=encoded_data.columns, fill_value=0)
    return encoded_user

def calculate_similarity(user_encoded, data_encoded):
    return cosine_similarity(user_encoded, data_encoded)



