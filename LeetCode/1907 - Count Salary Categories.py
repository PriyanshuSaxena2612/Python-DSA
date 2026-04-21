import pandas as pd
import numpy as np
def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    categories = ["Low Salary", "Average Salary", "High Salary"]
    accounts['category'] = np.where(
        accounts['income'] < 20000, "Low Salary",
        np.where(
            accounts['income'] > 50000, "High Salary",
            "Average Salary"
        )
    )
    accounts['category'] = pd.Categorical(accounts['category'], categories=categories)
    return accounts.groupby('category', as_index = False)[['income']].count().rename(columns = {
        'income': 'accounts_count' 
    })
