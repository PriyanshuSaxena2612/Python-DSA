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
```

**Do all of the following in a single chained expression:**

1. Standardise `category` to lowercase
2. Fill missing `amount` with the median amount of that category
3. Filter to only `success` transactions
4. Add a column `amount_bucket` — `'high'` if amount > 500, else `'low'`
5. Group by `category` and return the count of high vs low transactions per category as a clean DataFrame

**Expected shape of output:** a DataFrame with `category`, `amount_bucket`, and a count column.

---