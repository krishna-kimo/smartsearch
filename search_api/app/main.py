from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    term: str


app = FastAPI()

def make_retriever_req(query):
    pass

@app.post("/search/")
async def search_query(query: Item):
    return query.term
