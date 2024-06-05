import uvicorn
from fastapi import FastAPI, File, UploadFile
from recognizer import process_image
import os

app = FastAPI()


# if __name__ == "__main__":
#     uvicorn.run("main:app", port=8000, log_level="info")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/letter")
async def say_hello(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())
    return process_image(file_path)
