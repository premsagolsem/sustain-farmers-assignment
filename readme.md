## Install packages
```pip install -r requirements.txt```



## The FastAPI

Endpoint: /calculate_score
Method: POST
Request Body: JSON with the following fields
```{
  "family_id": "FAM001",
  "income": 100000,
  "savings": 20000,
  "monthly_expenses": 50000,
  "loan_payments": 5000,
  "credit_card_spending": [1000, 1200, 900, 800],
  "category_spending": {
    "Groceries": 2000,
    "Travel": 1500,
    "Entertainment": 1000
  },
  "financial_goals_met": 75
}
```

## Model Logic

The first i had calculated the financial score  based on several factors that represent a family’s financial health from the given data. Here’s the breakdown of the scoring logic that i used.

Savings-to-Income Ratio:
saving and income ratio is calculated using the below formula:

Formula: savings / income:
The higher this ratio, the better the financial health, as it suggests that the family is saving a significant portion of their income.

Monthly Expenses as a Percentage of Income is calculated using the formula that given below : 

Formula: monthly_expenses / income:
A lower percentage of monthly expenses relative to income is ideal. The higher this percentage, the more strained the financial situation.

 For the Loan Payments as a Percentage of Income are calculate using the given formula that given in bellow:

Formula: loan_payments / income
Lower loan payments as a percentage of income is preferred since it indicates the family is less burdened by debt.

Credit Card Spending Variability:
Formula: Standard deviation of credit card spending over time.
A high variability indicates inconsistent spending habits, which is considered a negative factor in the score.

Non-Essential Spending:
Non-essential spending includes categories like Travel, Entertainment, and Dining.
A higher ratio of non-essential spending reduces the financial health score.

Financial Goals Met (%):
Directly affects the score. A higher percentage of financial goals met indicates that the family is on track with their financial planning.
Formula for the Financial Score
The model combines the above factors with the following weighted scoring formula:

# Run Streamlit app

```streamlit run streamlit.py
```
