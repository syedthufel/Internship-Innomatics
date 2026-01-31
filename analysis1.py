import pandas as pd
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(os.path.join(script_dir, 'final_food_delivery_dataset.csv'))
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)

# 1
q1 = df[df['membership']=="Gold"].groupby('city')['total_amount'].sum().idxmax()

# 2
q2 = df.groupby('cuisine')['total_amount'].mean().idxmax()

# 3
user_totals = df.groupby('user_id')['total_amount'].sum()
count_users = (user_totals > 1000).sum()

# 4
df['rating_range'] = pd.cut(df['rating'], bins=[3,3.5,4,4.5,5], labels=["3.0–3.5","3.6–4.0","4.1–4.5","4.6–5.0"])
q4 = df.groupby('rating_range')['total_amount'].sum().idxmax()

# 5
q5 = df[df['membership']=="Gold"].groupby('city')['total_amount'].mean().idxmax()

# 6
rest_counts = df.groupby('cuisine')['restaurant_id'].nunique()
revenue = df.groupby('cuisine')['total_amount'].sum()
q6 = rest_counts.idxmin()

# 7
percent_gold = round((df[df['membership']=="Gold"].shape[0] / df.shape[0]) * 100)

# 8
# Use restaurant_name_x which comes from orders.csv and has actual names
# restaurant_name_y comes from restaurants.sql and has generic names like Restaurant_1
rest_stats = df.groupby('restaurant_name_x').agg(avg=('total_amount','mean'), cnt=('order_id','count'))
# Check specific restaurants from the options
restaurant_options = ['Grand Cafe Punjabi', 'Grand Restaurant South Indian', 
                     'Ruchi Mess Multicuisine', 'Ruchi Foods Chinese']
rest_stats_filtered = rest_stats[rest_stats.index.isin(restaurant_options) & (rest_stats['cnt']<20)]
if len(rest_stats_filtered) > 0:
    q8 = rest_stats_filtered.sort_values('avg', ascending=False).head(1).index[0]
else:
    # Fallback to overall max
    q8 = rest_stats[rest_stats['cnt']<20].sort_values('avg', ascending=False).head(1).index[0]

# Get details for all 4 restaurant options
q8_details = {}
for restaurant in restaurant_options:
    if restaurant in rest_stats.index:
        q8_details[restaurant] = {
            'avg': rest_stats.loc[restaurant, 'avg'],
            'count': rest_stats.loc[restaurant, 'cnt']
        }

# 9
# Check specific membership-cuisine combinations from the options
combo_revenue = df.groupby(['membership','cuisine'])['total_amount'].sum()
specific_combos = [
    ('Gold', 'Indian'),
    ('Gold', 'Italian'),
    ('Regular', 'Indian'),
    ('Regular', 'Chinese')
]
combo_values = {combo: combo_revenue.get(combo, 0) for combo in specific_combos}
q9 = max(combo_values, key=combo_values.get)
all_combo_max = df.groupby(['membership','cuisine'])['total_amount'].sum().idxmax()

# 10
df['quarter'] = df['order_date'].dt.to_period('Q')
q10 = df.groupby('quarter')['total_amount'].sum().idxmax()

# Print all results
print("=" * 60)
print("FOOD DELIVERY DATASET ANALYSIS RESULTS")
print("=" * 60)
print()
print(f"1. City with highest revenue from Gold members: {q1}")
print()
print(f"2. Cuisine with highest average order value: {q2}")
print()
print(f"3. Number of users with total spending > ₹1000: {count_users}")
print()
print(f"4. Rating range with highest total revenue: {q4}")
print()
print(f"5. City with highest avg order value for Gold members: {q5}")
print()
print(f"6. Cuisine with least number of restaurants: {q6}")
print()
print(f"7. Percentage of Gold membership orders: {percent_gold}%")
print()
print(f"8. Restaurant with highest avg revenue (<20 orders): {q8}")
print(f"   Restaurant details:")
if q8_details:
    for restaurant, details in sorted(q8_details.items(), key=lambda x: x[1]['avg'], reverse=True):
        count = details['count']
        avg = details['avg']
        status = " (<20 orders) ✓" if count < 20 else " (≥20 orders)"
        print(f"      {restaurant}: Avg ₹{avg:,.2f}, Orders: {int(count)}{status}")
else:
    print(f"      None of the specified restaurants found in dataset")
    print(f"      Checking similar restaurant names in data...")
    # Show restaurants with similar names
    for restaurant in restaurant_options:
        similar = [r for r in rest_stats.index if restaurant.lower() in r.lower() or r.lower() in restaurant.lower()]
        if similar:
            print(f"      Found similar to '{restaurant}': {similar[:3]}")
print()
print(f"9. Membership-Cuisine combo with max revenue (from options): {q9}")
print(f"   (Overall max combo in data: {all_combo_max})")
print(f"   Combo revenues:")
for combo, rev in sorted(combo_values.items(), key=lambda x: x[1], reverse=True):
    print(f"      {combo[0]} + {combo[1]}: ₹{rev:,.2f}")
print()
print(f"10. Quarter with highest total revenue: {q10}")
print()
print("=" * 60)
print("ADDITIONAL STATISTICS:")
print("=" * 60)

# 11. Total orders by Gold members
gold_orders_count = df[df['membership'] == 'Gold'].shape[0]
print(f"\n11. Total orders by Gold members: {gold_orders_count}")

# 12. Total revenue from Hyderabad city
hyderabad_revenue = round(df[df['city'] == 'Hyderabad']['total_amount'].sum())
print(f"\n12. Total revenue from Hyderabad: ₹{hyderabad_revenue:,}")

# 13. Distinct users who placed at least one order
distinct_users = df['user_id'].nunique()
print(f"\n13. Distinct users who placed at least one order: {distinct_users}")

# 14. Average order value for Gold members
gold_avg_order = round(df[df['membership'] == 'Gold']['total_amount'].mean(), 2)
print(f"\n14. Average order value for Gold members: ₹{gold_avg_order}")

# 15. Orders for restaurants with rating >= 4.5
high_rating_orders = df[df['rating'] >= 4.5].shape[0]
print(f"\n15. Orders for restaurants with rating ≥ 4.5: {high_rating_orders}")

# 16. Orders in top revenue city among Gold members only
# q1 already has the top revenue city for Gold members (Chennai)
orders_in_top_city_gold = df[(df['membership'] == 'Gold') & (df['city'] == q1)].shape[0]
print(f"\n16. Orders in {q1} (top revenue city for Gold members): {orders_in_top_city_gold}")

print()
print("=" * 60)
print("CHECKING RESTAURANT DATA:")
print("=" * 60)
print(f"\nColumn names in dataset: {list(df.columns)}")
print(f"\nRestaurant column being used: 'restaurant_name_x' (actual names from orders)")
print(f"\nSample restaurant names in data:")
print(df['restaurant_name_x'].unique()[:10])
print(f"\nTotal unique restaurants: {df['restaurant_name_x'].nunique()}")
print("\nTop 5 restaurants with <20 orders by avg revenue:")
top_5_rest = rest_stats[rest_stats['cnt']<20].sort_values('avg', ascending=False).head(5)
for idx, row in top_5_rest.iterrows():
    print(f"   {idx}: Avg ₹{row['avg']:,.2f}, Orders: {int(row['cnt'])}")
print("=" * 60)
