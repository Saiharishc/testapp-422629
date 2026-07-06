from fastapi import FastAPI

app = FastAPI(title="TestApp")

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/items')
async def list_items():
    return []

@app.get('/test')
async def test_endpoint():
    return {"message": "This is a test endpoint"}
