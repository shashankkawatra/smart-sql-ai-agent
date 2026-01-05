from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.dialects import SQLDialect
from app.prompt import build_prompt
from app.llm import generate_sql
from app.validator import validate_sql

app = FastAPI(title="Smart SQL AI Agent")

class SQLRequest(BaseModel):
    question: str
    dialect: SQLDialect

class SQLResponse(BaseModel):
    sql: str

@app.post("/generate-sql", response_model=SQLResponse)
def generate_sql_endpoint(req: SQLRequest):
    try:
        prompt = build_prompt(req.question, req.dialect)
        sql = generate_sql(prompt)
        validate_sql(sql)
        return SQLResponse(sql=sql)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
