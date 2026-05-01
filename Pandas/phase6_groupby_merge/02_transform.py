# ============================================================
# PHASE 6 — Groupby, Transform, Merge
# File    : 02_transform.py
# Topic   : transform — group stats without collapsing rows
# ============================================================

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "transaction_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "customer":       ["Raj", "Priya", "Amit", "Raj", "Priya", "Amit", "Neha", "Raj"],
    "amount":         [5000.0, 12000.0, 8000.0, 3200.0, 9500.0, 4500.0, 11000.0, 7800.0],
    "category":       ["food", "travel", "food", "travel", "electronics", "food", "travel", "electronics"],
    "status":         ["success", "success", "failed", "success", "success", "success", "success", "failed"],
    "city":           ["Delhi", "Mumbai", "Delhi", "Delhi", "Mumbai", "Bangalore", "Mumbai", "Delhi"]
})


# ── CONCEPT ─────────────────────────────────────────────────
#
# groupby + agg COLLAPSES rows — you get one row per group.
# groupby + transform KEEPS all rows — each row gets its
# group's calculated value broadcast back to it.
#
# The output of transform is ALWAYS the same length as the input.
#
# Visual:
#
#   Original (8 rows):           After agg (4 rows):
#   Raj    5000                  Raj    16000  ← one row per customer
#   Priya  12000                 Priya  21500
#   Amit   8000                  Amit   12500
#   Raj    3200                  Neha   11000
#   Priya  9500
#   Amit   4500
#   Neha   11000
#   Raj    7800
#
#   After transform (still 8 rows):
#   Raj    16000  ← Raj's total, pasted back to every Raj row
#   Priya  21500  ← Priya's total, pasted back to every Priya row
#   Amit   12500
#   Raj    16000
#   Priya  21500
#   Amit   12500
#   Neha   11000
#   Raj    16000
#
# Why is this useful?
#   You can add group-level context to each row.
#   e.g. "what % of this customer's total does this transaction represent?"
#   You need both the transaction amount AND the customer total on the same row.


# ── BASIC TRANSFORM ──────────────────────────────────────────

# Add each customer's total as a column
df["customer_total"] = df.groupby("customer")["amount"].transform("sum")
print(df[["customer", "amount", "customer_total"]])
#   customer   amount  customer_total
#        Raj   5000.0         16000.0
#      Priya  12000.0         21500.0
#       Amit   8000.0         12500.0
#        Raj   3200.0         16000.0  ← same total for all Raj rows
#      Priya   9500.0         21500.0
#       Amit   4500.0         12500.0
#       Neha  11000.0         11000.0
#        Raj   7800.0         16000.0

# String shortcuts for common aggregations
df["customer_mean"]   = df.groupby("customer")["amount"].transform("mean")
df["customer_max"]    = df.groupby("customer")["amount"].transform("max")
df["customer_min"]    = df.groupby("customer")["amount"].transform("min")
df["customer_count"]  = df.groupby("customer")["amount"].transform("count")
df["category_median"] = df.groupby("category")["amount"].transform("median")


# ── TRANSFORM WITH LAMBDA ────────────────────────────────────
#
# For custom logic, pass a lambda.
# Inside the lambda, x = one group's Series of values.

# Normalise amount within each customer group
# (amount - group min) / (group max - group min)
df["amount_normalised"] = df.groupby("customer")["amount"].transform(
    lambda x: (x - x.min()) / (x.max() - x.min())
)
print(df[["customer", "amount", "amount_normalised"]])

# Z-score within group: how many std deviations from group mean
df["amount_zscore"] = df.groupby("customer")["amount"].transform(
    lambda x: (x - x.mean()) / x.std()
)


# ── PRACTICAL USE CASES ──────────────────────────────────────

# 1. What % of this customer's total does each transaction represent?
df["customer_total"] = df.groupby("customer")["amount"].transform("sum")
df["pct_of_total"]   = (df["amount"] / df["customer_total"] * 100).round(2)
print(df[["customer", "amount", "customer_total", "pct_of_total"]])

# 2. How does each transaction compare to the category average?
df["cat_avg"]         = df.groupby("category")["amount"].transform("mean")
df["vs_cat_avg"]      = (df["amount"] - df["cat_avg"]).round(2)
print(df[["category", "amount", "cat_avg", "vs_cat_avg"]])

# 3. Rank transactions within each customer (highest first)
df["rank_in_customer"] = df.groupby("customer")["amount"].rank(
    ascending=False, method="dense"
).astype(int)
print(df[["customer", "amount", "rank_in_customer"]])


# ── FILL NULLS WITH GROUP STAT — THE DE PATTERN ─────────────
#
# The most common use of transform in Data Engineering.
# Fill missing values intelligently using the group's own stats.

df_with_nulls = pd.DataFrame({
    "customer": ["Raj", "Raj", "Priya", "Priya", "Amit"],
    "dept":     ["HR",  "HR",  "IT",    "IT",    "HR"],
    "salary":   [50000, None,  80000,   None,    60000]
})

# Wrong — fills with GLOBAL median (ignores department context)
df_with_nulls["salary_bad"] = df_with_nulls["salary"].fillna(
    df_with_nulls["salary"].median()
)

# Right — fills with the GROUP's median (context-aware)
df_with_nulls["salary_good"] = df_with_nulls.groupby("dept")["salary"].transform(
    lambda x: x.fillna(x.median())
)
print(df_with_nulls[["customer", "dept", "salary", "salary_bad", "salary_good"]])
# HR null gets HR median, IT null gets IT median

# Always add a fallback for groups that are entirely null
df_with_nulls["salary_good"] = df_with_nulls["salary_good"].fillna(
    df_with_nulls["salary_good"].median()
)


# ── TRANSFORM VS AGG — SIDE BY SIDE ─────────────────────────

# agg — one row per group
agg_result = df.groupby("customer")["amount"].sum().reset_index()
print("agg result shape:", agg_result.shape)    # (4, 2)

# transform — same rows as original
transform_result = df.groupby("customer")["amount"].transform("sum")
print("transform result shape:", transform_result.shape)  # (8,)
print("original df shape:", df.shape)                     # (8, ...)

# Key question to decide which to use:
# "Do I need a summary table?" → agg()
# "Do I need to add group info back to each row?" → transform()


# ── ROLLING TRANSFORM — time series context ──────────────────
#
# Rolling window per group — very common in financial data.
# Must use transform with a lambda for per-group rolling.

prices = pd.DataFrame({
    "stock":  ["RELIANCE"] * 5 + ["TCS"] * 5,
    "price":  [2500, 2520, 2480, 2510, 2550,
               3400, 3420, 3380, 3450, 3470]
})

# 3-day rolling average per stock
prices["rolling_3"] = prices.groupby("stock")["price"].transform(
    lambda x: x.rolling(3).mean()
)
print(prices)
# Without groupby, the rolling window would bleed across stocks


# ── COMMON MISTAKES ─────────────────────────────────────────

# MISTAKE 1: Using agg when you need transform
# You want to add group total as a column — don't do this:
totals = df.groupby("customer")["amount"].sum().reset_index()
df_wrong = df.merge(totals, on="customer", suffixes=("", "_total"))
# Works but unnecessarily complex — transform is cleaner:
df["customer_total"] = df.groupby("customer")["amount"].transform("sum")

# MISTAKE 2: Forgetting that transform returns a Series
result = df.groupby("customer")["amount"].transform("sum")
print(type(result))   # Series — assign it to a column

# MISTAKE 3: Not sorting before rolling transform
# Rolling window depends on row order.
# Always sort by date/time before applying rolling transforms.
prices = prices.sort_values(["stock", "price"])  # sort first
prices["rolling_3"] = prices.groupby("stock")["price"].transform(
    lambda x: x.rolling(3).mean()
)


# ── EXERCISE ─────────────────────────────────────────────────
#
# Use the df defined at the top of this file.
#
# 1. Add a column 'customer_total' showing each customer's
#    total amount across all their transactions.
#    Then add 'pct_of_customer_total' — what percentage of
#    their total each transaction represents. Round to 2dp.
#
# 2. Add a column 'category_avg' showing the average amount
#    for each category.
#    Then add 'above_category_avg' — True if the transaction
#    amount is above its category average, False otherwise.
#    (Do this with a vectorized comparison — no apply needed)
#
# 3. Rank each transaction within its customer group,
#    highest amount = rank 1.
#    Store in 'rank_in_customer'.
#    Then filter to only show each customer's top transaction
#    (rank == 1).
#
# 4. You have this DataFrame with nulls:
#
#    sales = pd.DataFrame({
#        "region":  ["North","North","South","South","East","East"],
#        "rep":     ["Raj","Priya","Amit","Neha","Kiran","Dev"],
#        "revenue": [50000, None, 80000, None, 60000, None]
#    })
#
#    Fill missing revenue with the region's median revenue.
#    Then verify no nulls remain.
#
# 5. Using the prices DataFrame from the notes above,
#    add a column 'daily_return' = pct_change per stock group.
#    Add another column 'rolling_3_avg' = 3-day rolling mean
#    per stock group.
#    Print the result.
#
# Write your code below this line:
# ─────────────────────────────────────────────────────────────

df = pd.DataFrame({
    "transaction_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "customer":       ["Raj", "Priya", "Amit", "Raj", "Priya", "Amit", "Neha", "Raj"],
    "amount":         [5000.0, 12000.0, 8000.0, 3200.0, 9500.0, 4500.0, 11000.0, 7800.0],
    "category":       ["food", "travel", "food", "travel", "electronics", "food", "travel", "electronics"],
    "status":         ["success", "success", "failed", "success", "success", "success", "success", "failed"],
    "city":           ["Delhi", "Mumbai", "Delhi", "Delhi", "Mumbai", "Bangalore", "Mumbai", "Delhi"]
})

df['customer_total'] = df.groupby('customer')["amount"].transform("sum")
df['pct_of_customer_total'] = round(df['amount']*100.00/df['customer_total'],2)

df['category_avg'] = df.groupby('category')["amount"].transform("mean")
df['above_category_avg'] = df['amount'] > df['category_avg']


df['rank_per_customer'] = df.groupby('customer')["amount"].rank(
        ascending=False
    ).astype(int)
print(df.query('rank_per_customer==1'))


sales = pd.DataFrame({
       "region":  ["North","North","South","South","East","East"],
       "rep":     ["Raj","Priya","Amit","Neha","Kiran","Dev"],
       "revenue": [50000, None, 80000, None, 60000, None]
   })

sales['revenue'] = sales.groupby('region')['revenue'].transform(lambda x: x.fillna(x.median()))
sales['revenue'] =  sales['revenue'].fillna(sales['revenue'].median())
print(sales['revenue'].isnull().sum())