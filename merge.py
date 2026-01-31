import pandas as pd
import sqlite3
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load files
orders = pd.read_csv(os.path.join(script_dir, 'orders.csv'))
users = pd.read_json(os.path.join(script_dir, 'users.json'))

# Load SQL file into sqlite
conn = sqlite3.connect(':memory:')
with open(os.path.join(script_dir, 'restaurants.sql'), 'r') as f:
    conn.executescript(f.read())

restaurants = pd.read_sql_query("SELECT * FROM restaurants", conn)

# Merge datasets
merged = orders.merge(users, on='user_id', how='left') \
               .merge(restaurants, on='restaurant_id', how='left')

# Save final dataset
output_path = os.path.join(script_dir, "final_food_delivery_dataset.csv")
merged.to_csv(output_path, index=False)

print(f"Dataset successfully merged and saved to: {output_path}")
print("\nFirst 5 rows:")
print(merged.head())
