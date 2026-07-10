from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory="src/elparadisogonzalo/static", html=True))

@app.get("/api")
def api():
    return {"project": "elparadisogonzalo"}
