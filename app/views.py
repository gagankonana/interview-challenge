from fastapi import APIRouter, FastAPI, File, UploadFile, Depends
from app.models import BusinessSymptomData, SessionLocal
from fastapi.responses import JSONResponse
import pandas as pd
import io
import csv



router = APIRouter()

@router.get("/business-symptom-data")
async def get_business_symptom_data(business_id: int = None, diagnostic: bool = None):
    try:
        db = SessionLocal()
        query = db.query(BusinessSymptomData)
        
        if business_id:
            query = query.filter(BusinessSymptomData.business_id == business_id)
        if diagnostic is not None:
            query = query.filter(BusinessSymptomData.symptom_diagnostic == diagnostic)
        data = query.all()
        return JSONResponse(content=[{"Business ID": d.business_id,
                                      "Business Name": d.business_name,
                                      "Symptom Code": d.symptom_code,
                                      "Symptom Name": d.symptom_name,
                                      "Symptom Diagnostic": d.symptom_diagnostic}
                                     for d in data])
    except Exception as e:
        return {'Error: ' + str(e)}

@router.post("/import_csv")
async def import_csv_data(file: UploadFile):
    
    try:
        db = SessionLocal()
        csv_data = file.file.read().decode('utf-8').splitlines()
        csv_rows = csv.reader(csv_data)
        data_list = []
        c = 0
        for row in csv_rows:
            # ignore column names
            if c == 0:
                c+=1
                continue

            # convert symptom_diagnostic into boolean values
            if row[4].lower() == "TRUE" or row[4] == "Yes":
                symptom_diagnostic = True
            else:
                symptom_diagnostic = False

            data = BusinessSymptomData(
                business_id=int(row[0]),
                business_name=row[1],
                symptom_code=row[2],
                symptom_name=row[3],
                symptom_diagnostic=symptom_diagnostic
            )
            data_list.append(data)

        db.add_all(data_list)
        db.commit()

        return {"status": "CSV data successfully imported."}

    except Exception as e:
        return {'Error: ' + str(e)}

@router.get('/status')
async def get_status():
    try:
        return {"Health OK"}

    except Exception as e:
        return {'Error: ' + str(e)}
