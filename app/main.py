from fastapi import FastAPI, HTTPException
from app.github import get_gists

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/{username}")
def list_gists(username: str):
    gists = get_gists(username)
    if gists is None:
        raise HTTPException(status_code=404, detail="User not found or no gists.")
    return gists
