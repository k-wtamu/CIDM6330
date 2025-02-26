pip install fastapi uvicorn


from fastapi import FastAPI # 1: import

app = FastAPI() # 2: make app


@app.get("/") # 3: path operation
async def root():
    return {"message": "Hello World"}
