import uvicorn
from fastapi import FastAPI
from user.router import router as user_router
from book.router import router as book_router

app = FastAPI()
app.include_router(user_router)
app.include_router(book_router)


@app.get("/")
async def main():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True, host="127.0.0.1")
