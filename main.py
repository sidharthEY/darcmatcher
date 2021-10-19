from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


from matcher import find_match

class PhraseModel(BaseModel):
    phrases: list

app = FastAPI()

@app.get("/")
def all_headings():
    from constants import LOOKUP_DICT
    return  {'headings': list(LOOKUP_DICT.keys())}

@app.post("/match")
def find_matches(all_phrases: PhraseModel):
    result_dict = dict()
    for item in all_phrases.phrases:
        result_dict[item] = find_match(item)
    return result_dict
