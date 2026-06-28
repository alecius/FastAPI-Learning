from fastapi import FastAPI,UploadFile,File
import shutil
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.post("/uploads")
async def upload_files(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}","wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    return{
        "message":"File uploaded successfully",
        "filename" : file.filename
    }

app.mount(      #mount create a folder url, we can look inside the upload folder by url
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)