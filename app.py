from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import uvicorn

from scoring_model import calculate_financial_score
app = FastAPI()
class TransactionData(BaseModel):
    family_id: str
    income: float
    savings: float
    monthly_expenses: float
    loan_payments: float
    credit_card_spending: list
    category_spending: dict
    financial_goals_met: float

@app.post("/calculate_score")
def calculate_financial_score(data: TransactionData):
    data_dict = data.dict()
    
    result = calculate_financial_score(data_dict)
    
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)