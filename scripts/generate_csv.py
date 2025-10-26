import csv
from datetime import datetime, timedelta
import random
import os

# Ensure raw_data folder exists
os.makedirs('../raw_data', exist_ok=True)

# Customers
with open('../raw_data/customers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['customer_id','name','email','region'])
    regions = ['North','South','East','West']
    for i in range(1, 51):
        writer.writerow([i, f'Customer {i}', f'customer{i}@example.com', regions[i%4]])

# Products
with open('../raw_data/products.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['product_id','name','category','price'])
    for i in range(101, 151):
        writer.writerow([i, f'Product {i-100}', f'Category {(i-101)%5 + 1}', (i-100)*10])

# Orders
start_date = datetime(2025, 10, 1)
with open('../raw_data/orders.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['order_id','customer_id','product_id','quantity','order_date'])
    for i in range(1001, 1051):
        customer_id = random.randint(1,50)
        product_id = random.randint(101,150)
        quantity = random.randint(1,5)
        order_date = (start_date + timedelta(days=(i-1001)%50)).strftime('%Y-%m-%d')
        writer.writerow([i, customer_id, product_id, quantity, order_date])
