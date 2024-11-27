import numpy as np

def calculate_financial_score(data):
    savings_ratio = data['savings'] / data['income']
    expense_ratio = data['monthly_expenses'] / data['income']
    loan_ratio = data['loan_payments'] / data['income']
    credit_card_variability = np.std(data['credit_card_spending'])
    non_essential_spending = sum(
        1 for cat, amt in data['category_spending'].items()
        if cat not in ['Groceries', 'Healthcare', 'Utilities']
    ) / sum(data['category_spending'].values())

    score = (
        0.25 * savings_ratio +
        0.20 * (1 - expense_ratio) +
        0.15 * (1 - loan_ratio) +
        0.15 * (1 - credit_card_variability) +
        0.15 * (1 - non_essential_spending) +
        0.10 * (data['financial_goals_met'] / 100)
    ) * 100

    insights = []
    if savings_ratio < 0.2:
        insights.append("Savings-to-Income ratio is low, affecting your score.")
    if expense_ratio > 0.3:
        insights.append("High monthly expenses reduce your score.")
    if non_essential_spending > 0.5:
        insights.append("Non-essential spending is high.")

    return {"score": round(score, 2), "insights": insights}
