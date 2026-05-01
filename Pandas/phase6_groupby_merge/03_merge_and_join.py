# ============================================================
# PHASE 6 — Groupby, Transform, Merge
# File    : 03_merge_and_join.py
# Topic   : Merging and joining DataFrames
# ============================================================

import pandas as pd
import numpy as np

# Two related tables — like a real database
orders = pd.DataFrame({
    "order_id":   [1001, 1002, 1003, 1004, 1005, 1006],
    "customer_id":[101,  102,  101,  103,  102,  104 ],
    "amount":     [5000, 12000, 8000, 3200, 9500, 4500],
    "status":     ["success","success","failed","success","success","success"]
})

customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 105],
    "name":        ["Raj", "Priya", "Amit", "Neha"],
    "city":        ["Delhi", "Mumbai", "Delhi", "Bangalore"]
})

# Notice:
#   customer_id 104 is in orders but NOT in customers
#   customer_id 105 is in customers but NOT in orders


# ── CONCEPT ─────────────────────────────────────────────────
#
# Merging combines two DataFrames using a common column.
# Exactly like SQL JOIN.
#
# Syntax:
#   pd.merge(left_df, right_df, on="common_column", how="join_type")
#
# The four join types:
#   inner  → only rows that match in BOTH tables
#   left   → all rows from left, matching rows from right (NaN if no match)
#   right  → all rows from right, matching rows from left (NaN if no match)
#   outer  → all rows from both, NaN where no match


# ── INNER JOIN — only matching rows ──────────────────────────
#
# SQL: SELECT * FROM orders INNER JOIN customers ON orders.customer_id = customers.customer_id

result = pd.merge(orders, customers, on="customer_id", how="inner")
print("INNER JOIN:")
print(result)
print(result.shape)  # (5, 6) — customer_id 104 dropped (not in customers)
                     #          customer_id 105 dropped (not in orders)

# Default is inner — how="inner" can be omitted
result = pd.merge(orders, customers, on="customer_id")
print(result.shape)  # same result


# ── LEFT JOIN — keep all left rows ───────────────────────────
#
# SQL: SELECT * FROM orders LEFT JOIN customers ON ...
# Use when: you want all orders, and customer info where available

result = pd.merge(orders, customers, on="customer_id", how="left")
print("\nLEFT JOIN:")
print(result)
# order_id 1006 (customer_id 104) stays — name and city are NaN
print(result.shape)   # (6, 6) — all 6 orders kept


# ── RIGHT JOIN — keep all right rows ─────────────────────────
#
# Keeps all customers, matching orders where available
result = pd.merge(orders, customers, on="customer_id", how="right")
print("\nRIGHT JOIN:")
print(result)
# customer_id 105 (Neha) appears with NaN for order columns
print(result.shape)   # (5, 6)

# Right join is rare — usually rewritten as a left join
# with tables swapped:
result = pd.merge(customers, orders, on="customer_id", how="left")
# same result, more readable


# ── OUTER JOIN — keep everything ─────────────────────────────
#
# All rows from both tables, NaN where no match
result = pd.merge(orders, customers, on="customer_id", how="outer")
print("\nOUTER JOIN:")
print(result)
print(result.shape)   # (7, 6) — customer 104 and 105 both kept


# ── DIFFERENT COLUMN NAMES ───────────────────────────────────
#
# When the join key has different names in each table
# use left_on and right_on

orders2 = pd.DataFrame({
    "order_id":  [1001, 1002, 1003],
    "cust_id":   [101, 102, 101],    # different name
    "amount":    [5000, 12000, 8000]
})

result = pd.merge(orders2, customers, left_on="cust_id", right_on="customer_id")
print(result)
# Both cust_id and customer_id columns appear in result
# Drop one if you don't need both:
result = result.drop(columns=["cust_id"])


# ── JOINING ON MULTIPLE COLUMNS ──────────────────────────────
#
# Pass a list to on= when the join requires multiple keys

inventory = pd.DataFrame({
    "product": ["A", "A", "B", "B"],
    "city":    ["Delhi", "Mumbai", "Delhi", "Mumbai"],
    "stock":   [100, 200, 150, 250]
})

sales_data = pd.DataFrame({
    "product": ["A", "A", "B"],
    "city":    ["Delhi", "Mumbai", "Delhi"],
    "sold":    [50, 80, 60]
})

result = pd.merge(inventory, sales_data, on=["product", "city"], how="left")
print(result)


# ── HANDLING DUPLICATE COLUMN NAMES ─────────────────────────
#
# When both tables have a column with the same name
# (other than the join key), Pandas adds suffixes.

orders_with_status = pd.DataFrame({
    "order_id":   [1001, 1002],
    "customer_id":[101, 102],
    "status":     ["success", "failed"]   # both tables have 'status'
})

customers_with_status = pd.DataFrame({
    "customer_id":[101, 102],
    "name":       ["Raj", "Priya"],
    "status":     ["active", "inactive"]  # conflict!
})

result = pd.merge(orders_with_status, customers_with_status, on="customer_id")
print(result.columns.to_list())
# ['order_id', 'customer_id', 'status_x', 'status_y']
# _x = from left table, _y = from right table

# Rename them immediately to avoid confusion
result = pd.merge(
    orders_with_status, customers_with_status,
    on="customer_id",
    suffixes=("_order", "_customer")
)
print(result.columns.to_list())
# ['order_id', 'customer_id', 'status_order', 'status_customer']


# ── MERGING AGGREGATED RESULTS ───────────────────────────────
#
# A common pattern — aggregate one table, merge back to original

# Add each customer's total order count to the orders table
customer_stats = (
    orders
    .groupby("customer_id")
    .agg(
        total_orders  = ("order_id", "count"),
        total_spent   = ("amount",   "sum")
    )
    .reset_index()
)

orders_enriched = pd.merge(orders, customer_stats, on="customer_id", how="left")
print(orders_enriched)

# This is the merge alternative to transform —
# use transform when you just need one stat back on the original
# use merge when you need multiple stats from a separate summary table


# ── concat — stacking DataFrames ─────────────────────────────
#
# concat stacks DataFrames vertically (row-wise) or horizontally.
# Use when you have multiple tables with the same structure
# that need to be combined into one.

jan = pd.DataFrame({"month": ["Jan"]*3, "amount": [1000, 2000, 3000]})
feb = pd.DataFrame({"month": ["Feb"]*3, "amount": [1500, 2500, 3500]})
mar = pd.DataFrame({"month": ["Mar"]*3, "amount": [1200, 2200, 3200]})

# Stack all months into one DataFrame
all_months = pd.concat([jan, feb, mar], ignore_index=True)
print(all_months)
print(all_months.shape)   # (9, 2)

# ignore_index=True — resets index to 0,1,2...
# Without it, index repeats: 0,1,2,0,1,2,0,1,2


# ── VALIDATE MERGE — catch unexpected duplicates ─────────────
#
# validate= checks if your join key is unique as expected.
# Catches bugs before they silently inflate your row count.

# "one_to_one"  → both keys are unique
# "one_to_many" → left key unique, right key can repeat
# "many_to_one" → left key can repeat, right key unique
# "many_to_many"→ both can repeat

try:
    result = pd.merge(
        orders, customers,
        on="customer_id",
        how="inner",
        validate="many_to_one"  # each customer appears once in customers
    )
    print("Merge validated successfully")
except pd.errors.MergeError as e:
    print(f"Merge validation failed: {e}")


# ── COMMON MISTAKES ─────────────────────────────────────────

# MISTAKE 1: Wrong join type losing rows silently
# If you expect all orders to appear but use inner join,
# orders with no matching customer are silently dropped.
# Always think: "which table's rows must ALL appear?"
# That table goes on the LEFT and you use how="left"

# MISTAKE 2: Not checking shape before and after merge
print("Before merge:", orders.shape)
result = pd.merge(orders, customers, on="customer_id", how="inner")
print("After merge:", result.shape)
# If after > before, you have duplicate keys causing row multiplication

# MISTAKE 3: Forgetting to reset_index after groupby before merging
# stats = df.groupby("customer_id")["amount"].sum()  # customer_id is INDEX
# # pd.merge(orders, stats, on="customer_id")  ← KeyError
# stats = stats.reset_index()  # now customer_id is a column ✓
# pd.merge(orders, stats, on="customer_id")

# MISTAKE 4: Duplicate column names creating _x _y confusion
# Always rename conflicting columns before or after merge
# using suffixes= parameter


# ── EXERCISE ─────────────────────────────────────────────────
#
# Use these three tables:

orders = pd.DataFrame({
    "order_id":    [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    "customer_id": [101,  102,  101,  103,  102,  104,  103 ],
    "product_id":  [201,  202,  203,  201,  203,  202,  204 ],
    "amount":      [5000, 12000, 8000, 3200, 9500, 4500, 6700],
    "status":      ["success","success","failed","success",
                    "success","success","success"]
})

customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 105],
    "name":        ["Raj", "Priya", "Amit", "Neha"],
    "city":        ["Delhi", "Mumbai", "Delhi", "Bangalore"]
})

products = pd.DataFrame({
    "product_id":   [201, 202, 203, 204],
    "product_name": ["Phone", "Laptop", "Tablet", "Watch"],
    "category":     ["electronics", "electronics", "electronics", "accessories"]
})

#
# 1. Inner join orders with customers on customer_id.
#    How many rows does the result have?
#    Which customer_id was dropped and why?
#
# 2. Left join orders with customers.
#    Which order has NaN for customer name?
#    Fill the missing name with "Unknown Customer".
#
# 3. Join all three tables together to get a full picture:
#    order_id, customer name, product name, amount, status.
#    Use two merges — first orders+customers, then +products.
#    Use inner join for both.
#
# 4. From the full joined table in question 3, find the
#    total amount per customer name.
#    Sort highest to lowest.
#
# 5. Using concat, stack orders with this new_orders table:
#
#    new_orders = pd.DataFrame({
#        "order_id":    [1008, 1009],
#        "customer_id": [101, 102],
#        "product_id":  [201, 204],
#        "amount":      [7500, 3800],
#        "status":      ["success", "success"]
#    })
#
#    Reset the index after concat.
#    Confirm the final shape.
#
# 6. Calculate total amount per customer_id from orders.
#    Merge this back onto the orders table as 'customer_total'.
#    Then add 'pct_of_total' — each order's % of that
#    customer's total. Round to 2dp.
#    (Hint: you can also do this with transform — try both)
#
# Write your code below this line:
# ─────────────────────────────────────────────────────────────

df_join1 = pd.merge(orders, customers, on = "customer_id", how = "inner")
print(df_join1) # 104 and 105 were dropped

df_join2 = pd.merge(orders, customers, on = "customer_id", how = "left").fillna("Unknown Customer")
print(df_join2) #104 is unknown

df_join3 = orders.merge(customers, on = "customer_id", how = "inner").merge(products, on="product_id", how = "inner")
print(df_join3[["order_id", "name", "product_name", "amount", "status"]])

print(
    df_join3.groupby("name")["amount"].sum().sort_values(ascending=False)
)


new_orders = pd.DataFrame({
       "order_id":    [1008, 1009],
       "customer_id": [101, 102],
       "product_id":  [201, 204],
       "amount":      [7500, 3800],
       "status":      ["success", "success"]
   })

df_join4 = pd.concat([orders, new_orders], ignore_index=True)
print(df_join4, df_join4.shape)

stats = orders.groupby('customer_id')['amount'].sum().reset_index()
df_join5 = pd.merge(orders, stats, on='customer_id',suffixes=("_order","_stats"))
df_join5['pct_of_total'] = round(df_join5['amount_order']*100/df_join5['amount_stats'],2)

df_join5['pct_of_total_02'] = orders.groupby('customer_id')['amount'].transform(lambda x: round(x*100/x.sum(),2))

print(df_join5)