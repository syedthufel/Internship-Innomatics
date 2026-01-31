import pandas as pd
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load final merged dataset
df = pd.read_csv(os.path.join(script_dir, 'final_food_delivery_dataset.csv'))

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)

print("Dataset Loaded Successfully\n")

# 1. Order trends over time (monthly)
df['month'] = df['order_date'].dt.to_period('M')
monthly_orders = df.groupby('month').size()
monthly_revenue = df.groupby('month')['total_amount'].sum()

print("Monthly Order Trend:")
print(monthly_orders)
print("\nMonthly Revenue Trend:")
print(monthly_revenue)

# 2. User behavior patterns
orders_per_user = df.groupby('user_id').size().sort_values(ascending=False)
avg_spend_per_user = df.groupby('user_id')['total_amount'].mean()

print("\nTop Users by Order Count:")
print(orders_per_user.head())

print("\nAverage Spend Per User:")
print(avg_spend_per_user.head())

# 3. City-wise performance
city_orders = df.groupby('city').size()
city_revenue = df.groupby('city')['total_amount'].sum()

print("\nCity-wise Orders:")
print(city_orders)

print("\nCity-wise Revenue:")
print(city_revenue)

# 4. Cuisine-wise performance
cuisine_orders = df.groupby('cuisine').size()
cuisine_revenue = df.groupby('cuisine')['total_amount'].sum()

print("\nCuisine-wise Orders:")
print(cuisine_orders)

print("\nCuisine-wise Revenue:")
print(cuisine_revenue)

# 5. Membership impact (Gold vs Regular)
membership_orders = df.groupby('membership').size()
membership_revenue = df.groupby('membership')['total_amount'].sum()
membership_avg_spend = df.groupby('membership')['total_amount'].mean()

print("\nMembership Order Count:")
print(membership_orders)

print("\nMembership Revenue:")
print(membership_revenue)

print("\nAverage Spend by Membership:")
print(membership_avg_spend)

# 6. Revenue distribution
print("\nRevenue Distribution:")
print(df['total_amount'].describe())

# 7. Seasonality (month-wise)
seasonality = df.groupby(df['order_date'].dt.month)['total_amount'].sum()

print("\nSeasonality (Month-wise Revenue):")
print(seasonality)
print("\nAnalysis Completed Successfully")