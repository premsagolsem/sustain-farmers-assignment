import streamlit as st
import pandas as pd
import numpy as np
from scoring_model import calculate_financial_score

st.title("Financial Health Scoring App")

st.sidebar.header("Input Financial Data")

family_id = st.sidebar.text_input("Family ID", value="FAM001")
income = st.sidebar.number_input("Monthly Income", min_value=0.0, value=50000.0, step=1000.0)
savings = st.sidebar.number_input("Savings", min_value=0.0, value=10000.0, step=500.0)
monthly_expenses = st.sidebar.number_input("Monthly Expenses", min_value=0.0, value=15000.0, step=500.0)
loan_payments = st.sidebar.number_input("Loan Payments", min_value=0.0, value=2000.0, step=100.0)
credit_card_spending = st.sidebar.text_area("Credit Card Spending (comma-separated)", value="1000,1200,900,800")
category_spending = st.sidebar.text_area(
    "Category Spending (e.g., {'Groceries': 500, 'Travel': 1500})",
    value="{'Groceries': 2000, 'Travel': 1500, 'Entertainment': 1000}"
)
financial_goals_met = st.sidebar.slider("Financial Goals Met (%)", 0, 100, 75)

try:
    credit_card_spending = [float(x) for x in credit_card_spending.split(",")]
    category_spending = eval(category_spending)
except Exception:
    st.error("Invalid input for Credit Card Spending or Category Spending. Please use valid formats.")

if st.sidebar.button("Calculate Financial Score"):
    input_data = {
        "family_id": family_id,
        "income": income,
        "savings": savings,
        "monthly_expenses": monthly_expenses,
        "loan_payments": loan_payments,
        "credit_card_spending": credit_card_spending,
        "category_spending": category_spending,
        "financial_goals_met": financial_goals_met
    }

    result = calculate_financial_score(input_data)

    st.subheader("Financial Score")
    st.metric(label="Score", value=result["score"])
    st.subheader("Insights")
    for insight in result["insights"]:
        st.write(f"- {insight}")

    st.subheader("Recommendations")
    if "Savings-to-Income ratio is low" in result["insights"]:
        recommended_savings = income * 0.2  # Suggest 20% savings
        savings_deficit = max(0, recommended_savings - savings)
        st.write(f"Increase savings by at least ${savings_deficit:.2f} to improve your score.")
    if "High monthly expenses" in result["insights"]:
        recommended_expenses = income * 0.3  # Suggest 30% max on expenses
        expense_reduction = max(0, monthly_expenses - recommended_expenses)
        st.write(f"Reduce monthly expenses by at least ${expense_reduction:.2f} to improve your score.")
    if "Non-essential spending is high" in result["insights"]:
        st.write("Reduce discretionary spending by 10% to boost your score.")

st.subheader("Spending Visualization")


if category_spending:
    category_df = pd.DataFrame(category_spending.items(), columns=["Category", "Amount"])
    st.bar_chart(category_df.set_index("Category"))

