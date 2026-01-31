import pandas as pd
import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# Load all source files
orders = pd.read_csv(os.path.join(script_dir, 'orders.csv'))
users = pd.read_json(os.path.join(script_dir, 'users.json'))

conn = sqlite3.connect(':memory:')
with open(os.path.join(script_dir, 'restaurants.sql'), 'r') as f:
    conn.executescript(f.read())
restaurants = pd.read_sql_query("SELECT * FROM restaurants", conn)

# Load final merged dataset
final_df = pd.read_csv(os.path.join(script_dir, 'final_food_delivery_dataset.csv'))

print("=" * 70)
print("MERGE QUESTIONS ANALYSIS")
print("=" * 70)

# Q1: Column to join orders and users
print("\n1. The column used to join orders.csv and users.json:")
print(f"   Answer: user_id")
print(f"   (Common columns: {set(orders.columns) & set(users.columns)})")

# Q2: Format of cuisine and rating dataset
print("\n2. The dataset containing cuisine and rating information is stored in:")
print(f"   Answer: SQL format")
print(f"   (restaurants.sql contains columns: {list(restaurants.columns)})")

# Q3: Total rows in final merged dataset
print(f"\n3. The total number of rows in the final merged dataset:")
print(f"   Answer: {len(final_df)}")

# Q4: Missing user records
print("\n4. If a user has no matching record in users.json:")
print(f"   Answer: NaN (or null)")
print(f"   (Using left join: orders.merge(users, on='user_id', how='left'))")

# Q5: Pandas function to combine datasets
print("\n5. The Pandas function used to combine datasets based on a key:")
print(f"   Answer: merge")

# Q6: Origin of membership column
print("\n6. The column 'membership' originates from:")
users_cols = list(users.columns)
print(f"   Answer: users.json")
print(f"   (users.json columns: {users_cols})")
print(f"   ('membership' in users: {'membership' in users_cols})")

# Q7: Join key for restaurant details
print("\n7. The join key used to combine orders data with restaurant details:")
print(f"   Answer: restaurant_id")
print(f"   (Common columns: {set(orders.columns) & set(restaurants.columns)})")

# Q8: Column identifying food type
print("\n8. The column that identifies the type of food served by a restaurant:")
print(f"   Answer: cuisine")
print(f"   (Restaurant columns: {list(restaurants.columns)})")

# Q9: Multiple orders by same user
# Find a user with multiple orders
user_order_counts = orders.groupby('user_id').size()
user_with_multiple = user_order_counts[user_order_counts > 1].index[0]
order_count = user_order_counts[user_with_multiple]
appearances = final_df[final_df['user_id'] == user_with_multiple].shape[0]

print(f"\n9. If a user places multiple orders, their personal details appear:")
print(f"   Answer: {order_count} times (same as number of orders)")
print(f"   (Example: User {user_with_multiple} placed {order_count} orders,")
print(f"    their details appear {appearances} times in final dataset)")

print("\n" + "=" * 70)
