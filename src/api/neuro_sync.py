from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Добро пожаловать в ESNSeY API"}

@app.get("/status")
def get_status():
    return {"system": "ESNSeY v4.0", "status": "active"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
