# Food Delivery Dataset Analysis

A comprehensive data analysis project that merges multiple data sources and performs detailed analytics on food delivery operations across multiple Indian cities.

## 📋 Project Overview

This project analyzes food delivery data by merging information from three different sources:
- **Orders Data** (CSV): Order transactions with restaurant details
- **User Data** (JSON): Customer information including membership status
- **Restaurant Data** (SQL): Restaurant details including cuisine and ratings

The analysis provides insights into order trends, user behavior, city-wise performance, cuisine preferences, and membership impact on revenue.

## 📂 Project Structure

```
Infomatics Intern/
│
├── 📓 Jupyter Notebooks
│   ├── merge.ipynb           # Data merging workflow
│   ├── analysis.ipynb        # Comprehensive analysis
│   └── analysis1.ipynb       # Quiz questions & answers
│
├── 🐍 Python Scripts
│   ├── merge.py              # Merge datasets script
│   ├── analysis.py           # Full analysis script
│   ├── analysis1.py          # Quiz analysis script
│   ├── check_data.py         # Data verification utility
│   └── merge_questions.py    # Merge process Q&A
│
├── 📊 Data Files
│   ├── orders.csv            # Order transactions
│   ├── users.json            # User information
│   ├── restaurants.sql       # Restaurant database
│   └── final_food_delivery_dataset.csv  # Merged dataset
│
├── 🔧 Environment
│   └── venv/                 # Python virtual environment
│
└── README.md                 # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.13 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/syedthufel/Internship-Innomatics.git
   cd Internship-Innomatics
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install pandas jupyter sqlite3
   ```

## 📊 Dataset Description

### Source Files

1. **orders.csv** (10,000 rows)
   - `order_id`: Unique order identifier
   - `user_id`: Customer identifier
   - `restaurant_id`: Restaurant identifier
   - `order_date`: Date of order (DD-MM-YYYY)
   - `total_amount`: Order value in ₹
   - `restaurant_name`: Name of restaurant

2. **users.json** (2,883 users)
   - `user_id`: Unique user identifier
   - `name`: Customer name
   - `city`: Customer city (Bangalore, Chennai, Hyderabad, Pune)
   - `membership`: Gold or Regular

3. **restaurants.sql** (500 restaurants)
   - `restaurant_id`: Unique restaurant identifier
   - `restaurant_name`: Generic name (Restaurant_1, Restaurant_2, etc.)
   - `cuisine`: Chinese, Indian, Italian, Mexican
   - `rating`: Rating from 3.0 to 5.0

### Merged Dataset

The final merged dataset contains **10,000 rows** with all columns from the three sources, using left joins to preserve all order records.

## 🔄 Data Merging Process

The merging follows this workflow:

```python
# Step 1: Load data from three sources
orders = pd.read_csv('orders.csv')
users = pd.read_json('users.json')
restaurants = pd.read_sql_query("SELECT * FROM restaurants", conn)

# Step 2: Merge using left joins
merged = orders.merge(users, on='user_id', how='left') \
               .merge(restaurants, on='restaurant_id', how='left')

# Step 3: Save final dataset
merged.to_csv('final_food_delivery_dataset.csv', index=False)
```

**Key Joining Columns:**
- `user_id`: Links orders with user information
- `restaurant_id`: Links orders with restaurant details

## 📈 Analysis & Insights

### Key Questions Answered

1. **Which city has the highest total revenue from Gold members?**
   - **Answer:** Chennai

2. **Which cuisine has the highest average order value?**
   - **Answer:** Mexican

3. **How many users have total spending > ₹1000?**
   - **Answer:** 2,544 users (> 2000 category)

4. **Which rating range generates the highest revenue?**
   - **Answer:** 4.6–5.0

5. **Which city has highest avg order value for Gold members?**
   - **Answer:** Chennai

6. **Which cuisine has the least number of restaurants?**
   - **Answer:** Chinese

7. **What percentage of orders are from Gold members?**
   - **Answer:** 50%

8. **Best performing restaurant with <20 orders?**
   - **Answer:** Ruchi Foods Chinese (₹686.60 avg, 19 orders)

9. **Which membership-cuisine combo has max revenue?**
   - **Answer:** Gold + Italian (₹1,005,779.05)

10. **Which quarter has the highest revenue?**
    - **Answer:** Q3 2023 (Jul-Sep)

### Additional Statistics

- **Total Gold member orders:** 4,987
- **Hyderabad total revenue:** ₹1,889,367
- **Distinct users:** 2,883
- **Gold member avg order value:** ₹797.15
- **Orders for restaurants rated ≥4.5:** 3,374
- **Orders in Chennai (top Gold city):** 1,337

## 🎯 Usage

### Running Jupyter Notebooks

```bash
jupyter notebook
```

Then open:
- `merge.ipynb` - Step-by-step data merging
- `analysis.ipynb` - Comprehensive analysis
- `analysis1.ipynb` - Quiz questions with solutions

### Running Python Scripts

```bash
# Merge datasets
python merge.py

# Run comprehensive analysis
python analysis.py

# Get quiz answers
python analysis1.py

# Check merge process details
python merge_questions.py
```

## 📊 Analysis Categories

### 1. Order Trends
- Monthly order counts
- Monthly revenue trends
- Quarterly performance
- Seasonality analysis

### 2. User Behavior
- Orders per user distribution
- Average spend per user
- High-value customers (>₹1000 total)
- Membership impact (Gold vs Regular)

### 3. City-wise Performance
- Order volume by city
- Revenue by city
- Gold member concentration
- Average order values

### 4. Cuisine Analysis
- Popular cuisines
- Revenue by cuisine type
- Average order values by cuisine
- Restaurant distribution

### 5. Restaurant Performance
- Top performing restaurants
- Rating-wise revenue distribution
- High-potential low-volume restaurants
- Restaurant density by cuisine

## 🛠️ Technologies Used

- **Python 3.13**
- **Pandas** - Data manipulation and analysis
- **SQLite3** - SQL database handling
- **Jupyter Notebook** - Interactive analysis
- **Git** - Version control

## 📝 Merge Process Q&A

**Q: What column joins orders.csv and users.json?**  
A: `user_id`

**Q: What format stores cuisine and rating information?**  
A: SQL format (restaurants.sql)

**Q: Total rows in final merged dataset?**  
A: 10,000

**Q: What happens when a user has no matching record?**  
A: NaN (null values) - using left join

**Q: Pandas function used to combine datasets?**  
A: `merge()`

**Q: Where does the membership column originate?**  
A: users.json file

**Q: Join key for restaurant details?**  
A: `restaurant_id`

**Q: Column identifying food type?**  
A: `cuisine`

**Q: How many times do user details appear for multiple orders?**  
A: Same number as their order count (duplicated for each order)

## 🤝 Contributing

This is an internship project. For suggestions or improvements, please open an issue or submit a pull request.

## 👨‍💻 Author

**Syed Thufel**
- GitHub: [@syedthufel](https://github.com/syedthufel)
- Repository: [Internship-Innomatics](https://github.com/syedthufel/Internship-Innomatics)

## 📄 License

This project is part of an internship program at Innomatics Research Labs.

## 🙏 Acknowledgments

- Innomatics Research Labs for the internship opportunity
- The data analysis project specifications and requirements

---

**Last Updated:** January 31, 2026

**Project Status:** ✅ Complete
