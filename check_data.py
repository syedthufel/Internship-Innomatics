import pandas as pd
import sqlite3

# Check restaurants
conn = sqlite3.connect(':memory:')
with open('restaurants.sql', 'r') as f:
    conn.executescript(f.read())
restaurants = pd.read_sql_query('SELECT * FROM restaurants', conn)

print('Restaurants columns:', list(restaurants.columns))
print('\nFirst 10 restaurants:')
print(restaurants.head(10))

# Check orders
orders = pd.read_csv('orders.csv')
print('\n\nOrders columns:', list(orders.columns))
print('\nFirst 5 orders with restaurant names:')
print(orders[['order_id', 'restaurant_id', 'restaurant_name']].head(10))

# Check if the issue is in column names during merge
print('\n\nChecking column overlap:')
print('Orders has restaurant_name:', 'restaurant_name' in orders.columns)
print('Restaurants has restaurant_name:', 'restaurant_name' in restaurants.columns)
