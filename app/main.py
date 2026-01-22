from fastapi import FastAPI ,File, UploadFile
import uvicorn
import pandas as pd
from app_services import validation 
import Data_Processing
import db

app = FastAPI()

@app.get("/")
def root():
    return {"healty"}

@app.on_event("startup")
def init():
    db.create_db()

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    validation(file=file)
    df = Data_Processing.get_df(file.file)
    count = len(df)
    db.init_db()
    res = db.save_records(df.to_dict("records"))
    return {"status": "success","inserted_records": count}


if __name__=="__main__":
    uvicorn.run("main:app" , host="0.0.0.0",port=8000,reload=True)