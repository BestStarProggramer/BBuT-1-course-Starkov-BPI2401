from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

wikipedia.set_lang("en")

app = FastAPI()

class ArticleResponse(BaseModel):
    title: str
    summary: str

class SearchRequest(BaseModel):
    query: str

@app.get("/articles/{title}", response_model=ArticleResponse)
def get_article(title: str):

    """Get article by title"""
    
    return {
        "title": title,
        "summary": wikipedia.summary(title)
     }
    

@app.get("/search/", response_model=list[str])
def search_articles(query: str, limit: int = 5):

    """Search for articles by query"""

    return wikipedia.search(query, results=limit)


@app.post("/random/", response_model=ArticleResponse)
def get_random_article(request: SearchRequest):

    """Get a random article"""

    title = wikipedia.random()
    return {
        "title": title,
        "summary": wikipedia.summary(title)
    }