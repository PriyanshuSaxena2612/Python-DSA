import pandas as pd
import numpy as np

df = pd.DataFrame({
    'transaction_id': range(1, 21),
    'customer_id':    [101, 102, 103, 101, 104, 102, 105, 103, 101, 104,
                       102, 105, 103, 101, 104, 102, 105, 103, 101, 104],
    'amount':         [250.5, None, 1200.0, 85.0, None, 430.0, 75.5, 920.0,
                       None, 310.0, 640.0, None, 180.0, 2100.0, None, 390.0,
                       55.0, 760.0, None, 480.0],
    'category':       ['food', 'travel', 'electronics', 'food', 'travel',
                       'FOOD', 'Electronics', 'travel', 'FOOD', 'electronics',
                       'Travel', 'food', 'ELECTRONICS', 'travel', 'food',
                       'electronics', 'TRAVEL', 'food', 'electronics', 'travel'],
    'status':         ['success', 'success', 'failed', 'success', 'pending',
                       'success', 'failed', 'success', 'pending', 'success',
                       'success', 'failed', 'success', 'success', 'pending',
                       'success', 'success', 'failed', 'success', 'success'],
    'txn_date':       pd.date_range(start='2024-01-01', periods=20, freq='D')
})

result = (
    df
    # Step 1 — lowercase category FIRST, before any groupby
    .assign(category=lambda x: x['category'].str.lower())

    # Step 2 — fill nulls with per-category median
    # must be a separate assign because amount depends on updated category
    .assign(amount=lambda x: x['amount'].fillna(
        x.groupby('category')['amount'].transform('median')
    ))

    # Step 3 — keep only successful transactions
    .query("status == 'success'")

    # Step 4 — bucket amount into high / low
    .assign(amount_bucket=lambda x: np.where(x['amount'] > 500, 'high', 'low'))

    # Step 5 — count high vs low per category
    .groupby(['category', 'amount_bucket'])
    .size()
    .reset_index(name='count')
)

print(result)