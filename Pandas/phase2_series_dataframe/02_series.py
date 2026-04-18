# ============================================================
# PHASE 2 — Series and DataFrame
# File    : 02_series.py
# Topic   : Series — one column of data
# ============================================================

import pandas as pd
import numpy as np


# ── CONCEPT ─────────────────────────────────────────────────
#
# A Series is a one-dimensional labelled array.
# Think of it as a single column from a spreadsheet —
# it has values AND a label for each value (the index).
#
# List vs Series:
#
#   Plain list:
#     [50000, 60000, 75000]
#     - values only
#     - no labels
#     - no built-in math operations
#     - slow on large data
#
#   Pandas Series:
#     0    50000
#     1    60000
#     2    75000
#     dtype: int64
#     - values AND labels (the index)
#     - built-in math, statistics, string ops
#     - handles missing values gracefully
#     - very fast on large data
#
# Every column in a DataFrame IS a Series.
# When you do df['salary'], you get a Series back.


# ── CREATING A SERIES ────────────────────────────────────────

# From a list — index is 0, 1, 2... by default
salaries = pd.Series([50000, 60000, 75000])
print(salaries)
# 0    50000
# 1    60000
# 2    75000
# dtype: int64

# From a list with a custom index
salaries = pd.Series(
    [50000, 60000, 75000],
    index=["Alice", "Bob", "Charlie"]
)
print(salaries)
# Alice      50000
# Bob        60000
# Charlie    75000
# dtype: int64

# With a name — useful when the Series becomes a DataFrame column
salaries = pd.Series(
    [50000, 60000, 75000],
    name="salary"
)
print(salaries.name)   # "salary"

# From a dict — keys become the index, values become the data
salaries = pd.Series({"Alice": 50000, "Bob": 60000, "Charlie": 75000})
print(salaries)
# Alice      50000
# Bob        60000
# Charlie    75000


# ── THE INDEX ────────────────────────────────────────────────
#
# The index is the label on each row.
# By default it's 0, 1, 2... (called RangeIndex).
# You can set it to anything — names, dates, IDs.
#
# The index is how Pandas aligns data when you combine Series.

s = pd.Series([10, 20, 30])
print(s.index)    # RangeIndex(start=0, stop=3, step=1)

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s.index)    # Index(['a', 'b', 'c'], dtype='object')


# ── ACCESSING VALUES ─────────────────────────────────────────

salaries = pd.Series(
    [50000, 60000, 75000],
    index=["Alice", "Bob", "Charlie"]
)

# By label (using the index)
print(salaries["Alice"])    # 50000
print(salaries["Bob"])      # 60000

# By position (like a list)
print(salaries.iloc[0])     # 50000  — first item
print(salaries.iloc[-1])    # 75000  — last item

# Multiple values — pass a list of labels
print(salaries[["Alice", "Charlie"]])
# Alice      50000
# Charlie    75000

# Slicing by position
print(salaries.iloc[0:2])
# Alice    50000
# Bob      60000


# ── SERIES ATTRIBUTES ────────────────────────────────────────
#
# Attributes give you information ABOUT the Series.
# No parentheses needed — they're properties, not methods.

s = pd.Series([50000, 60000, None, 75000])

print(s.dtype)     # float64  (None makes it float)
print(s.shape)     # (4,)     — 4 rows, 1 dimension
print(len(s))      # 4        — total rows including nulls
print(s.count())   # 3        — non-null rows only
print(s.index)     # RangeIndex(start=0, stop=4, step=1)
print(s.values)    # [50000. 60000.   nan 75000.]  — plain numpy array


# ── BUILT-IN STATISTICS ──────────────────────────────────────
#
# Series has statistics built in — no loops needed.
# These all ignore NaN by default.

salaries = pd.Series([50000, 60000, 75000, np.nan, 45000])

print(salaries.sum())      # 230000.0
print(salaries.mean())     # 57500.0
print(salaries.median())   # 55000.0
print(salaries.min())      # 45000.0
print(salaries.max())      # 75000.0
print(salaries.std())      # standard deviation
print(salaries.describe()) # all stats at once


# ── VECTORISED OPERATIONS ────────────────────────────────────
#
# This is what makes Pandas fast.
# Operations apply to every value at once — no loop needed.

salaries = pd.Series([50000, 60000, 75000])

# Add 5000 to every salary — no loop
print(salaries + 5000)
# 0    55000
# 1    65000
# 2    80000

# Give everyone a 10% raise
print(salaries * 1.1)
# 0    55000.0
# 1    66000.0
# 2    82500.0

# Compare every value — returns a Series of True/False
print(salaries > 55000)
# 0    False
# 1     True
# 2     True

# This True/False Series is what powers filtering in DataFrames.
# df[df['salary'] > 55000] works because of exactly this.


# ── MISSING VALUES IN A SERIES ───────────────────────────────

s = pd.Series([100, np.nan, 200, None, 300])
print(s)
# 0    100.0
# 1      NaN
# 2    200.0
# 3      NaN
# 4    300.0

# Both np.nan and None become NaN in a numeric Series.

# Check which values are missing
print(s.isna())
# 0    False
# 1     True
# 2    False
# 3     True
# 4    False

# Count missing values
print(s.isna().sum())    # 2

# Fill missing values
print(s.fillna(0))       # replace NaN with 0
print(s.fillna(s.mean())) # replace NaN with mean

# Drop missing values
print(s.dropna())        # returns Series without NaN rows


# ── VALUE COUNTS ─────────────────────────────────────────────
#
# Counts how many times each unique value appears.
# Very useful for categorical columns.

departments = pd.Series(["HR", "IT", "HR", "Finance", "IT", "HR"])
print(departments.value_counts())
# HR         3
# IT         2
# Finance    1
# dtype: int64

# As percentages
print(departments.value_counts(normalize=True))
# HR         0.500000
# IT         0.333333
# Finance    0.166667


# ── APPLYING A FUNCTION TO A SERIES ──────────────────────────
#
# .apply() calls your function on every value in the Series.
# This is where Phase 1's functions and lambdas connect to Pandas.

salaries = pd.Series([50000, 60000, 75000])

# Using a named function
def add_bonus(x):
    return x * 1.1

print(salaries.apply(add_bonus))
# 0    55000.0
# 1    66000.0
# 2    82500.0

# Using a lambda — same result, one line
print(salaries.apply(lambda x: x * 1.1))

# Using a lambda with a condition
print(salaries.apply(lambda x: "high" if x > 55000 else "low"))
# 0     low
# 1    high
# 2    high


# ── COMMON MISTAKES ─────────────────────────────────────────

# MISTAKE 1: Confusing .count() and len()
s = pd.Series([10, 20, np.nan, 30])
print(len(s))      # 4  — includes NaN
print(s.count())   # 3  — excludes NaN
# Use len() for total rows, count() for non-null rows.

# MISTAKE 2: Forgetting that operations return a NEW Series
s = pd.Series([1, 2, 3])
s + 10             # this does nothing — result is thrown away
s = s + 10         # correct — assign back to s
print(s)           # [11, 12, 13]

# MISTAKE 3: Using a loop when vectorised operation works
salaries = pd.Series([50000, 60000, 75000])

# SLOW — unnecessary loop
result = []
for s in salaries:
    result.append(s * 1.1)

# FAST — vectorised
result = salaries * 1.1


# ── EXERCISE ─────────────────────────────────────────────────
#
# 1. Create a Series called 'prices' with these values:
#      120.5, 85.0, np.nan, 200.0, 95.5, np.nan, 150.0
#    Give it this custom index:
#      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#
# 2. Print:
#      - total number of values (including nulls)
#      - number of non-null values
#      - mean, min, max (all ignore nulls automatically)
#
# 3. Print only the missing values — rows where value is NaN.
#    Hint: use isna() to get a True/False Series,
#    then use it to filter prices.
#
# 4. Fill the missing values with the median of the Series.
#    Store the result in a new variable called prices_clean.
#    Verify no nulls remain using isna().sum().
#
# 5. Using a lambda and .apply(), create a new Series called
#    'price_category' from prices_clean where:
#      value < 100   → "budget"
#      value < 160   → "mid"
#      value >= 160  → "premium"
#    Print price_category.
#
# 6. Print the value_counts() of price_category.
#    How many items fall in each category?
#
# Write your code below this line:
# ─────────────────────────────────────────────────────────────

prices = pd.Series\
    ([120.5, 85.0, np.nan, 200.0, 95.5, np.nan, 150.0], \
     index = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], \
        name = "prices")
print(prices)

print(len(prices))
print(prices.count())
print(prices.mean(), prices.min(), prices.max())
print(prices[prices.isna()])
prices_clean = prices.fillna(prices.median())
print(prices_clean.isna().sum())
price_category = \
    prices_clean\
        .apply\
            (lambda x: "budget" if x<100 else \
             ("mid" if x >=100 and x <160 else "premium"))
print(price_category)
print(price_category.value_counts())