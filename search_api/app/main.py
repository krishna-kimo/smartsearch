from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json

class Item(BaseModel):
    term: str


app = FastAPI()

def make_ret_search(entities):
    url = "http://34.107.125.154:8081/postretriever/"
    payload = {}
    payload['input'] = {}
    payload['input']['queryTerms'] = [entities['query'].lower()]
    payload['input']['numOfRetrievedRecords'] = 10
    payload['input']['allowedContentTypes'] = [entities['content_type'].lower()]

    res = requests.post(url=url, data=json.dumps(payload))

    return res.json()
    #return json.dumps(payload)
def parse_entities(jsonObj):
    req_entities = {}
    for entity in jsonObj['entities']:
        if entity['entity'] == "content_type":
            req_entities['content_type'] = entity['value']
        elif entity['entity'] == "search_term":
            req_entities['query'] = entity['value']
        ## Add time later

    return req_entities

def fetch_entities(query):
    url = "http://rasa:5005/model/parse"
    payload = {}
    payload['text'] = "Articles for Machine learning for 5 min"

    res = requests.post(url=url, data=json.dumps(payload)) 
    entities = parse_entities(res.json())

    res = make_ret_search(entities)

    return res
    #return "Fuck you"


@app.post("/")
async def greet():
    return "hello"


@app.post("/search/")
async def search_query(query: Item):
    return fetch_entities(query.term)
