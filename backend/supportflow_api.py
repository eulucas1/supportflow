from fastapi import FastAPI

app = FastAPI(title="SupportFlow")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
