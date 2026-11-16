"""
Practice Task 08: Sales Data Aggregator and Business Metrics Calculator

Problem Statement:
Write a Python program that processes a list of transaction dictionaries, 
aggregates total revenue, calculates average order values, and identifies 
the top-performing product category. 

Exercise Purpose:
This bridges basic Python logic with core Data Analytics and business intelligence 
concepts. In data analytics and AI programs, you must be able to clean, group, 
and extract meaningful KPI summaries from raw transactional datasets.

Example:
    Input: List of transaction records with category, price, and quantity.
    Output: Total Revenue, Average Order Value, and Best-Selling Category.
"""

def analyze_sales_data(transactions):
    """Calculates total revenue, average order value, and top category."""
    if not transactions:
        return {"total_revenue": 0.0, "average_order_value": 0.0, "top_category": None}

    total_revenue = 0.0
    category_sales = {}
    
    for txn in transactions:
        revenue = txn["price"] * txn["quantity"]
        total_revenue += revenue
        
        cat = txn["category"]
        category_sales[cat] = category_sales.get(cat, 0.0) + revenue
        
    avg_order_value = total_revenue / len(transactions)
    top_category = max(category_sales, key=category_sales.get)
    
    return {
        "total_revenue": round(total_revenue, 2),
        "average_order_value": round(avg_order_value, 2),
        "top_category": top_category,
        "category_breakdown": category_sales
    }


if __name__ == "__main__":
    sample_transactions = [
        {"item": "Laptop", "category": "Electronics", "price": 1200.00, "quantity": 1},
        {"item": "Mouse", "category": "Electronics", "price": 25.50, "quantity": 3},
        {"item": "Desk Chair", "category": "Furniture", "price": 150.00, "quantity": 2},
        {"item": "Notebook", "category": "Stationery", "price": 5.00, "quantity": 10},
        {"item": "Monitor", "category": "Electronics", "price": 300.00, "quantity": 2}
    ]
    
    print("Processing Sales Transactions...")
    metrics = analyze_sales_data(sample_transactions)
    
    print(f"Total Revenue: ${metrics['total_revenue']:,}")
    print(f"Average Order Value: ${metrics['average_order_value']:,}")
    print(f"Top Category: {metrics['top_category']}")