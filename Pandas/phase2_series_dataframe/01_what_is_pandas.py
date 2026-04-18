# ============================================================
# PHASE 2 — Series and DataFrame
# File    : 01_what_is_pandas.py
# Topic   : What is Pandas and why does it exist
# ============================================================


# ── CONCEPT ─────────────────────────────────────────────────
#
# Pandas is a Python library for working with tabular data.
# A library is code someone else wrote that you can use
# by importing it.
#
# Think of Pandas as Excel inside Python — but:
#   - Handles millions of rows (Excel struggles past ~100k)
#   - Can be automated — no clicking, just code
#   - Connects to databases, APIs, files of any format
#   - Plugs into every other data tool in Python
#
# Without Pandas, analysing data in Python means writing
# hundreds of lines of loops and dicts manually.
# Pandas gives you those operations in one line.
#
# Who uses Pandas:
#   Data Analysts     → explore and summarise data
#   Data Engineers    → clean and move data between systems
#   Data Scientists   → prepare data for models
#   Quant Researchers → analyse financial time series


# ── INSTALLATION ─────────────────────────────────────────────
#
# If you haven't installed Pandas yet, run this in your terminal:
#   pip install pandas
#
# You only do this once. After that, you just import it.


# ── IMPORTING PANDAS ─────────────────────────────────────────
#
# 'import' loads the library so you can use it.
# 'as pd' gives it a short nickname — pd.
# Every Pandas user in the world uses 'pd' as the alias.
# Never use a different alias — it confuses everyone.

import pandas as pd

# From now on, every time you write pd.something,
# you are using a tool from the Pandas library.

print(pd.__version__)   # prints the Pandas version you have installed


# ── WHAT PANDAS GIVES YOU ────────────────────────────────────
#
# Two main objects — everything in Pandas is one of these:
#
#   Series     → one column of data (a list with superpowers)
#   DataFrame  → a full table of data (a dict of lists with superpowers)
#
# We will cover both in detail in the next two files.
# For now, just see what they look like:

# A Series — one column
s = pd.Series([50000, 60000, 75000])
print(s)
# 0    50000
# 1    60000
# 2    75000
# dtype: int64
#
# The numbers on the left (0, 1, 2) are the INDEX.
# The numbers on the right are the VALUES.
# dtype: int64 means all values are integers.

# A DataFrame — a full table
df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Charlie"],
    "salary": [50000,   60000, 75000]
})
print(df)
#       name  salary
# 0    Alice   50000
# 1      Bob   60000
# 2  Charlie   75000
#
# Row numbers on the left are the INDEX.
# Column names at the top are from your dict keys.


# ── WHERE DOES DATA COME FROM ────────────────────────────────
#
# In real work you rarely create DataFrames by hand.
# Data comes from files or databases:
#
#   pd.read_csv("file.csv")         → reads a CSV file
#   pd.read_excel("file.xlsx")      → reads an Excel file
#   pd.read_json("file.json")       → reads a JSON file
#   pd.read_parquet("file.parquet") → reads a Parquet file
#   pd.read_sql("SELECT...", conn)  → reads from a database
#
# We will cover all of these in Phase 3.
# For now we create DataFrames by hand to learn the concepts.


# ── NUMPY — PANDAS' FOUNDATION ───────────────────────────────
#
# Pandas is built on top of another library called NumPy.
# NumPy handles fast number crunching under the hood.
# You will import it alongside Pandas in almost every file:

import numpy as np

# np.nan is how Pandas represents a missing value (like None but for numbers)
# You'll use this constantly when dealing with real dirty data.

print(np.nan)          # nan
print(type(np.nan))    # <class 'float'>

# np.nan is different from None:
#   None  → Python's general "no value"
#   np.nan → NumPy's "missing number" — works inside numeric calculations

# print(None + 0)     # TypeError — can't add None to a number
print(np.nan + 0)   # nan — doesn't crash, propagates the "missing" signal


# ── THE PANDAS WORKFLOW ──────────────────────────────────────
#
# Every data task in Pandas follows this pattern:
#
#   1. Load   → read data from a file or database into a DataFrame
#   2. Explore → understand what the data looks like
#   3. Clean  → fix types, handle nulls, remove duplicates
#   4. Transform → filter, group, join, calculate
#   5. Export → write results to a file or database
#
# This is the loop you will repeat for every project.
# Each phase in this course covers one step of this workflow.


# ── COMMON MISTAKES ─────────────────────────────────────────

# MISTAKE 1: Importing with the wrong alias
# import pandas as pandas  ← works but nobody does this
# import pandas as p       ← works but confuses other developers
# Always use: import pandas as pd

# MISTAKE 2: Forgetting to install before importing
# If you see "ModuleNotFoundError: No module named 'pandas'"
# it means Pandas isn't installed.
# Fix: run   pip install pandas   in your terminal, then try again.

# MISTAKE 3: Confusing np.nan and None
# In Pandas, missing numeric values are np.nan, not None.
# When you check for missing values you use:
#   pd.isna(value)   → works for both np.nan and None
#   value is None    → only catches None, misses np.nan
# We will cover this properly in Phase 7.


# ── EXERCISE ─────────────────────────────────────────────────
#
# Short one — this file is mostly conceptual.
#
# 1. Import pandas as pd and numpy as np.
#    Print the version of pandas using pd.__version__
#
# 2. Create a Series called 'temperatures' with these values:
#      32.5, 35.0, 31.2, 33.8, 36.1
#    Print it.
#
# 3. Create a DataFrame called 'weather' from a dict with
#    these columns and values:
#      day         → ["Mon", "Tue", "Wed", "Thu", "Fri"]
#      temperature → [32.5, 35.0, 31.2, 33.8, 36.1]
#      humidity    → [80, 75, 85, 70, 65]
#    Print it.
#
# 4. Print the type of 'temperatures' using type().
#    Print the type of 'weather' using type().
#    What is the difference?
#
# 5. Create a list with one np.nan value in it:
#      [100, np.nan, 200]
#    Try adding 50 to each item using a list comprehension.
#    What happens to the np.nan item?
#    Print the result.
#
# Write your code below this line:
# ─────────────────────────────────────────────────────────────
import pandas as pd
import numpy as np
print(pd.__version__)
temperatures = pd.Series([32.5, 35.0, 31.2, 33.8, 36.1])
print(temperatures)

weather = pd.DataFrame(
    {
        "day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "temperature": [32.5, 35.0, 31.2, 33.8, 36.1],
        "humidity": [80, 75, 85, 70, 65]
    }
)
print(weather)
print(type(temperatures), type(weather))
np_list = [100, np.nan, 200]
np_list_add = [x+50 for x in np_list]
print(np_list_add)