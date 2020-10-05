from typing import Optional

import uvicorn
from fastapi import FastAPI

from server.controllers import cerveja_controller
from server.repositories.cerveja_repository import CervejaRepository

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


app.include_router(cerveja_controller.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
