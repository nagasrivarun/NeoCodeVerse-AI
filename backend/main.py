from fastapi import FastAPI

app = FastAPI(title="NeoCodeVerse AI API")


@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Welcome to NeoCodeVerse AI!"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
