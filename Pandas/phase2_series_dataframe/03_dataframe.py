# ============================================================
# PHASE 2 — Series and DataFrame
# File    : 03_dataframe.py
# Topic   : DataFrame — a full table of data
# ============================================================

import pandas as pd
import numpy as np


# ── CONCEPT ─────────────────────────────────────────────────
#
# A DataFrame is a two-dimensional table with:
#   - Rows    → each row is one record (one employee, one transaction)
#   - Columns → each column is one attribute (name, salary, date)
#   - Index   → the label for each row (0, 1, 2... by default)
#
# Think of it as:
#   - A spreadsheet you can manipulate with code
#   - A SQL table you can query with Python
#   - A dict of Series — each column is a Series
#
# Relationship between dict, Series, and DataFrame:
#
#   dict of lists
#       ↓  pd.DataFrame()
#   DataFrame
#       ↓  df['column']
#   Series  (one column)
#       ↓  series.values
#   numpy array  (raw numbers)


# ── CREATING A DATAFRAME ─────────────────────────────────────

# Most common way — from a dict of lists
df = pd.DataFrame({
    "name":       ["Alice", "Bob", "Charlie", "Diana"],
    "department": ["HR",    "IT",  "HR",      "Finance"],
    "salary":     [50000,   60000, 55000,     70000],
    "is_active":  [True,    True,  False,     True]
})
print(df)
#       name department  salary  is_active
# 0    Alice         HR   50000       True
# 1      Bob         IT   60000       True
# 2  Charlie         HR   55000      False
# 3    Diana    Finance   70000       True


# From a list of dicts — each dict is one row
rows = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob",   "salary": 60000},
]
df2 = pd.DataFrame(rows)
print(df2)
#     name  salary
# 0  Alice   50000
# 1    Bob   60000

# With a custom index
df3 = pd.DataFrame(
    {"name": ["Alice", "Bob"], "salary": [50000, 60000]},
    index=[101, 102]   # employee IDs as index
)
print(df3)
#       name  salary
# 101  Alice   50000
# 102    Bob   60000


# ── DATAFRAME ATTRIBUTES ─────────────────────────────────────
#
# These give you information ABOUT the DataFrame.
# No parentheses — they are properties not methods.

df = pd.DataFrame({
    "name":       ["Alice", "Bob", "Charlie", "Diana"],
    "department": ["HR",    "IT",  "HR",      "Finance"],
    "salary":     [50000,   60000, 55000,     70000],
    "is_active":  [True,    True,  False,     True]
})

print(df.shape)    # (4, 4)  → (rows, columns)
print(df.columns)  # Index(['name', 'department', 'salary', 'is_active'])
print(df.index)    # RangeIndex(start=0, stop=4, step=1)
print(df.dtypes)   # dtype of each column
print(len(df))     # 4  → number of rows


# ── EXPLORING A DATAFRAME ────────────────────────────────────
#
# These are the first things you run whenever new data arrives.

print(df.head())     # first 5 rows (default)
print(df.head(2))    # first 2 rows
print(df.tail())     # last 5 rows
print(df.tail(2))    # last 2 rows
print(df.sample(2))  # 2 random rows — useful for spot checking

print(df.info())
# Prints column names, non-null counts, dtypes.
# First thing to run on any new dataset.

print(df.describe())
# Summary statistics for numeric columns only.
# Shows count, mean, std, min, 25%, 50%, 75%, max.


# ── A DATAFRAME IS A DICT OF SERIES ──────────────────────────
#
# Each column is a Series living inside the DataFrame.
# When you pull out a column, you get a Series back.

salary_series = df["salary"]
print(type(salary_series))   # <class 'pandas.core.series.Series'>
print(salary_series)
# 0    50000
# 1    60000
# 2    55000
# 3    70000

# You can verify this by checking the columns dict-style
print(df.keys())   # same as df.columns


# ── ACCESSING COLUMNS ────────────────────────────────────────

# Single column → returns a Series
print(df["name"])

# Multiple columns → returns a DataFrame
print(df[["name", "salary"]])

# Dot notation — works but NOT recommended
print(df.name)     # same as df["name"] but breaks if column has spaces


# ── ACCESSING ROWS ───────────────────────────────────────────
#
# Two ways — loc and iloc.
# We will cover these in full detail in Phase 4.
# For now just know they exist.

print(df.iloc[0])      # first row by position
print(df.iloc[0:2])    # first two rows by position
print(df.loc[0])       # row with index label 0


# ── ADDING A NEW COLUMN ──────────────────────────────────────
#
# Two ways. Both work — we will cover assign() properly in Phase 5.

# Way 1 — direct assignment
df["salary_k"] = df["salary"] / 1000
print(df)

# Way 2 — assign() returns a new DataFrame, doesn't modify original
df2 = df.assign(salary_k=df["salary"] / 1000)

# Way 1 modifies df in place.
# Way 2 leaves df untouched and gives you a new DataFrame.
# In pipelines, Way 2 is preferred — safer.


# ── RENAMING COLUMNS ─────────────────────────────────────────

df_renamed = df.rename(columns={
    "name":       "employee_name",
    "department": "dept"
})
print(df_renamed.columns)
# Index(['employee_name', 'dept', 'salary', 'is_active', 'salary_k'])


# ── DROPPING COLUMNS ─────────────────────────────────────────

df_dropped = df.drop(columns=["salary_k"])
print(df_dropped.columns)
# Index(['name', 'department', 'salary', 'is_active'])

# Original df is unchanged — drop returns a new DataFrame
print("salary_k" in df.columns)   # True — still in original


# ── NULL VALUES IN A DATAFRAME ───────────────────────────────

df_with_nulls = pd.DataFrame({
    "name":   ["Alice", "Bob",  "Charlie"],
    "salary": [50000,   None,   75000],
    "dept":   ["HR",    "IT",   None]
})

# Count nulls per column
print(df_with_nulls.isna().sum())
# name      0
# salary    1
# dept      1

# Percentage null per column
print(df_with_nulls.isna().mean() * 100)

# Which rows have ANY null
print(df_with_nulls[df_with_nulls.isna().any(axis=1)])
#     name   salary dept
# 1    Bob      NaN   IT
# 2  Charlie  75000  None


# ── BASIC DATAFRAME INFO PATTERN ─────────────────────────────
#
# This is the sequence you run every single time
# you receive new data. Memorise it.

def explore(df):
    print("Shape:   ", df.shape)
    print("Columns: ", list(df.columns))
    print("Dtypes:\n",   df.dtypes)
    print("Nulls:\n",    df.isna().sum())
    print("Sample:\n",   df.head())

explore(df)


# ── COMMON MISTAKES ─────────────────────────────────────────

# MISTAKE 1: Single vs double brackets for columns
print(type(df["salary"]))     # Series   ← single bracket
print(type(df[["salary"]]))   # DataFrame ← double bracket
# Use single when you want a Series (for calculations)
# Use double when you want a DataFrame (to keep table structure)

# MISTAKE 2: Forgetting that most operations return a NEW DataFrame
df_copy = df.drop(columns=["salary_k"])
# df is unchanged — you must assign the result

# MISTAKE 3: Modifying a slice
# Never do this — it triggers a SettingWithCopyWarning:
# df[df['salary'] > 50000]['salary'] = 999
# We will cover the correct way (loc) in Phase 4.

# MISTAKE 4: Dot notation with column names that have spaces
# df.my column  ← SyntaxError
# df["my column"]  ← always works
# Avoid column names with spaces entirely in real work.


# ── EXERCISE ─────────────────────────────────────────────────
#
# 1. Create a DataFrame called 'transactions' with these columns:
#      transaction_id → [1001, 1002, 1003, 1004, 1005]
#      customer       → ["Raj", "Priya", "Amit", "Neha", "Raj"]
#      amount         → [5000.0, 12000.0, None, 8500.0, 3200.0]
#      category       → ["food", "travel", "food", None, "travel"]
#      status         → ["success", "success", "failed", "success", "success"]
#
# 2. Run the full exploration sequence on it:
#      shape, columns, dtypes, null counts, head
#
# 3. Pull out the 'amount' column as a Series.
#    Confirm its type using type().
#    Print its mean, ignoring nulls.
#
# 4. Pull out only 'customer' and 'amount' as a DataFrame.
#    Confirm its type using type().
#
# 5. Add a new column 'amount_usd' = amount divided by 83
#    (rough INR to USD conversion).
#    Round it to 2 decimal places using .round(2).
#
# 6. Print only the rows that have ANY null value.
#    How many are there?
#
# 7. Write an explore() function (like the one above)
#    and call it on your transactions DataFrame.
#
# Write your code below this line:
# ─────────────────────────────────────────────────────────────


transactions = pd.DataFrame(
    {
        "transaction_id" : [1001, 1002, 1003, 1004, 1005],
        "customer"       : ["Raj", "Priya", "Amit", "Neha", "Raj"],
        "amount"         : [5000.0, 12000.0, None, 8500.0, 3200.0],
        "category"       : ["food", "travel", "food", None, "travel"],
        "status"         : ["success", "success", "failed", "success", "success"]
    }
)

def explore_dataframe(df):
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.to_list()}")
    print(f"dtypes: \n{df.dtypes}")
    print(f"null count: \n{df.isna().sum()}")
    print(f"sample: \n{df.head()}")
explore_dataframe(transactions)

print
(
    f"Amount Column: \n{transactions['amount']}",
    type(transactions['amount']),
    "\n",transactions[transactions["amount"].notna()]["amount"].mean()
)

print(
    transactions[["customer","amount"]],"\n",
    type(transactions[["customer","amount"]])
)

transactions["amount_usd"] = round(transactions["amount"] / 83,2)
print(transactions)

print(transactions[transactions.isna().any(axis=1)])