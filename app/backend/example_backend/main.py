from fastapi import FastAPI
import random
import string
import typing
import uvicorn
from starlette.middleware.cors import CORSMiddleware

alph = string.ascii_letters + string.digits + string.punctuation

def gen_string():
    return ''.join(random.SystemRandom().choice(alph) for _ in range(random.randint(3, 20)))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


items = [gen_string() for _ in range(1000)]

@app.get("/items/{search_term}/", response_model=typing.List[str])
def read_item(search_term: str):
    search_term = search_term.lower()
    return [
        item for item in items
        if search_term in item.lower()
    ]


def run_app():
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level="info")

if __name__ == '__main__':
    run_app()
    