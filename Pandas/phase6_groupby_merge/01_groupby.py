# ============================================================
# PHASE 6 — Groupby, Transform, Merge
# File    : 01_groupby.py
# Topic   : Groupby and aggregation
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
# Groupby splits your DataFrame into groups based on a column,
# then you do something to each group.
#
# It follows three steps — always in this order:
#
#   1. SPLIT   → divide rows into groups
#   2. APPLY   → calculate something on each group
#   3. COMBINE → bring results back together
#
# SQL equivalent:
#   SELECT customer, SUM(amount)
#   FROM transactions
#   GROUP BY customer
#
# Pandas:
#   df.groupby("customer")["amount"].sum()
#
# Reading it out loud:
#   "Group the DataFrame by customer,
#    look at the amount column,
#    take the sum of each group"


# ── SINGLE AGGREGATION ───────────────────────────────────────

# Total amount per customer
print(df.groupby("customer")["amount"].sum())

# Average amount per category
print(df.groupby("category")["amount"].mean())

# Count of transactions per city
print(df.groupby("city")["transaction_id"].count())

# All basic aggregations
print(df.groupby("customer")["amount"].sum())
print(df.groupby("customer")["amount"].mean())
print(df.groupby("customer")["amount"].max())
print(df.groupby("customer")["amount"].min())
print(df.groupby("customer")["amount"].median())
print(df.groupby("customer")["amount"].count())  # non-null only
print(df.groupby("customer")["amount"].std())    # standard deviation


# ── size() vs count() ────────────────────────────────────────
#
# This is a common source of confusion.
#
# size()  → counts ALL rows per group including nulls
# count() → counts only NON-NULL rows per group
#
# When your data has no nulls, they give the same result.
# When your data has nulls, they differ.

print(df.groupby("customer").size())             # all rows
print(df.groupby("customer")["amount"].count())  # non-null rows


# ── MULTIPLE AGGREGATIONS — agg() ────────────────────────────
#
# agg() lets you calculate multiple things at once.
# Each line inside agg() follows this pattern:
#
#   new_column_name = ("source_column", "aggregation_function")

result = df.groupby("customer").agg(
    total_amount   = ("amount", "sum"),
    avg_amount     = ("amount", "mean"),
    max_amount     = ("amount", "max"),
    txn_count      = ("transaction_id", "count"),
    unique_cities  = ("city", "nunique")   # nunique = count of unique values
)
print(result)

# reset_index() flattens the group key back into a regular column
result = df.groupby("customer").agg(
    total_amount = ("amount", "sum")
).reset_index()
print(result)
#   customer  total_amount
# 0     Amit        12500.0
# 1     Neha        11000.0
# 2    Priya        21500.0
# 3      Raj        16000.0


# ── GROUP BY MULTIPLE COLUMNS ────────────────────────────────

# Total amount per customer per category
result = df.groupby(["customer", "category"])["amount"].sum().reset_index()
print(result)

# Average amount per city per status
result = df.groupby(["city", "status"])["amount"].mean().reset_index()
print(result)


# ── FILTERING AFTER GROUPBY ──────────────────────────────────
#
# Two ways to filter after aggregation.

# Way 1 — query() after reset_index()
result = (
    df.groupby("customer")["amount"]
    .sum()
    .reset_index()
    .query("amount > 15000")
)
print(result)

# Way 2 — boolean mask on the aggregated result
result = df.groupby("customer")["amount"].sum().reset_index()
result = result[result["amount"] > 15000]
print(result)


# ── GROUPBY + filter() — keep entire groups ──────────────────
#
# filter() keeps or drops ENTIRE GROUPS based on a condition.
# Different from query() which filters individual rows.
#
# x = one group's DataFrame inside the lambda

# Keep only customers who have more than 2 transactions
result = df.groupby("customer").filter(lambda x: len(x) > 2)
print(result)
# Only Raj (3 txns) and Priya, Amit (2 each — so only Raj here)

# Keep only cities where average amount > 7000
result = df.groupby("city").filter(lambda x: x["amount"].mean() > 7000)
print(result)


# ── GROUPBY ON A FILTERED DATAFRAME ─────────────────────────
#
# You can filter first, then group.
# This is the pattern for "group by X, but only for Y rows"

# Total amount per customer for successful transactions only
result = (
    df[df["status"] == "success"]
    .groupby("customer")["amount"]
    .sum()
    .reset_index()
)
print(result)


# ── NAMED AGGREGATION vs DICT STYLE ─────────────────────────
#
# Two styles of agg() — both valid, named style is cleaner.

# Named style (preferred — you control output column names)
df.groupby("customer").agg(
    total = ("amount", "sum"),
    count = ("amount", "count")
)

# Dict style (older style — column names are harder to control)
df.groupby("customer").agg({"amount": ["sum", "count"]})
# Creates MultiIndex columns — harder to work with
# Prefer named style in all new code


# ── WHAT GROUPBY RETURNS ─────────────────────────────────────
#
# groupby() on its own returns a GroupBy object — not a DataFrame.
# You must call an aggregation on it to get a result.

g = df.groupby("customer")
print(type(g))   # DataFrameGroupBy — not a DataFrame yet

# You can iterate over groups — useful sometimes
for name, group in df.groupby("customer"):
    print(f"\nCustomer: {name}")
    print(group[["amount", "status"]])


# ── COMMON MISTAKES ─────────────────────────────────────────

# MISTAKE 1: Forgetting reset_index()
result = df.groupby("customer")["amount"].sum()
# customer is now the INDEX not a column
# result["customer"]  ← KeyError — it's the index, not a column
result = result.reset_index()
# now customer is a regular column ✓

# MISTAKE 2: Using count() when you want size()
# count() skips nulls — if amount has nulls, count gives wrong totals
# size() always counts all rows
df.groupby("customer").size()             # safer for row counts
df.groupby("customer")["amount"].count()  # for non-null counts specifically

# MISTAKE 3: Trying to use the result before reset_index
result = df.groupby("customer")["amount"].sum()
# result is a Series with customer as index
# To merge it back or filter it as a column, reset_index first

# MISTAKE 4: Grouping by a column with nulls
# Rows where the group column is null are DROPPED by default
# df.groupby("city", dropna=False) — include null as a group


# ── EXERCISE ─────────────────────────────────────────────────
#
# Use the df defined at the top of this file.
#
# 1. Find the total amount spent per customer.
#    Sort the result from highest to lowest.
#
# 2. For each category, find:
#      - total amount
#      - average amount
#      - number of transactions
#      - number of unique customers
#    Use agg() with named columns.
#
# 3. Find total amount per customer but ONLY for
#    successful transactions.
#    Filter first, then groupby.
#
# 4. Using groupby + filter(), keep only cities
#    where the TOTAL amount across all transactions
#    is greater than 15000.
#    Print the filtered DataFrame.
#
# 5. Group by both customer AND status.
#    Find the count of transactions for each combination.
#    Reset the index and print the result.
#
# 6. From the result of question 1, filter to only
#    customers whose total is above 10000.
#    Use query().
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

print(
    df.groupby('customer')["amount"].sum().sort_values(ascending=False)
)

print(
    df.groupby('category').agg(
        total_amount = ("amount","sum"),
        average_amount = ("amount","mean"),
        number_of_transactions = ("amount","count"),
        number_of_unique_customers = ("customer","nunique")
    )\
    .reset_index()
)

print(
    df[df['status'].str.lower() == 'success']\
    .groupby('customer')\
    ["amount"].sum()\
    .reset_index()
)

print(
    df.groupby('city')\
    .filter(lambda x: x["amount"].sum()>15000)\
    .reset_index()
)

print(
    df.groupby(["customer","status"])\
    .agg(
        count_transactions = ("transaction_id","count")
    ).reset_index()
)

print(
    df.groupby('customer')["amount"].sum()\
    .reset_index()\
    .query("amount>10000")\
    .sort_values(by="amount",ascending=False)
)