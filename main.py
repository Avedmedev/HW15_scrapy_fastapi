from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from db.connect import get_db
from src.router import articles

app = FastAPI()


@app.get("/api/healthchecker")
async def healthchecker(db: Session = Depends(get_db)):
    try:
        r = db.execute('SELECT 1').fetchone()
        if r is None:
            raise HTTPException(status_code=500, detail='Database is not configured correctly')
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail='Error connection to database')


app.include_router(articles.router, prefix='/api')


@app.get("/")
def read_root():
    return {"message": "News integrator API v1.01"}
