import pandas as pd
# Import pandas library for data handling and analysis

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv(
    'D:\\naman\\2026- AI, CODE\\Report generator project\\report_data.csv'
)
# Read the CSV file and load it into a pandas DataFrame

# Convert Date column into datetime format
df['Date'] = pd.to_datetime(df['Date'])
# This allows us to extract month, year, and perform date-based analysis

# Preview first 5 rows of the dataset
print(df.head())
# Helps verify that data is loaded correctly

# -----------------------------
# Basic Calculations
# -----------------------------
total_records = len(df)
# Total number of transactions

total_amount = df['Amount'].sum()
# Total money involved (sales + expenses)

average_amount = df['Amount'].mean()
# Average transaction value

max_amount = df['Amount'].max()
# Highest transaction amount

min_amount = df['Amount'].min()
# Lowest transaction amount

# -----------------------------
# Separate Sales vs Expense
# -----------------------------
sales_total = df[df['Category'] == 'Sales']['Amount'].sum()
# Filter only sales rows and calculate total sales

expense_total = df[df['Category'] == 'Expense']['Amount'].sum()
# Filter only expense rows and calculate total expenses

net_profit = sales_total - expense_total
# Calculate net profit by subtracting expenses from sales

# -----------------------------
# Monthly Summary
# -----------------------------
df['Month'] = df['Date'].dt.to_period('M')
# Extract month and year from date (example: 2024-01)

monthly_summary = df.groupby('Month')['Amount'].sum()
# Group transactions by month and calculate total amount per month

# -----------------------------
# Payment Method Breakdown
# -----------------------------
payment_summary = df.groupby('Payment_Method')['Amount'].sum()
# Calculate total amount received/spent per payment method

# -----------------------------
# Generate Business Report
# -----------------------------
report = f"""
BUSINESS FINANCIAL REPORT
========================

TOTAL OVERVIEW
--------------
Total Records        : {total_records}
Total Amount         : {total_amount:.2f}
Average Amount       : {average_amount:.2f}
Maximum Amount       : {max_amount:.2f}
Minimum Amount       : {min_amount:.2f}

SALES VS EXPENSE
----------------
Total Sales          : {sales_total:.2f}
Total Expenses       : {expense_total:.2f}
Net Profit           : {net_profit:.2f}

MONTHLY SUMMARY
---------------
{monthly_summary.to_string()}

PAYMENT METHOD BREAKDOWN
------------------------
{payment_summary.to_string()}
"""
# Create a clean, readable business report using formatted text

# Print report to console
print(report)

# Save report to a text file
with open("business_report.txt", "w") as f:
    f.write(report)
# This allows sharing the report with managers or storing records
