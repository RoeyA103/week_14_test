from fastapi import HTTPException , UploadFile

def validation(file:UploadFile):
    if not file:
        raise HTTPException(status_code=400,detail="No file provided")
    if not file.filename.lower().endswith(('.csv',".xlsx",".xls")):
        raise HTTPException(status_code=400,detail="Invalid CSV file")
    

