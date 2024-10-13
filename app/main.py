from fastapi import FastAPI

from app.db.create_db import create_all_tables

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    create_all_tables()
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
