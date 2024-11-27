from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.all_routes import api_router
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(api_router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=False
    )
