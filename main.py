basket = [
    {"Product": "Leather wallet", "Unit Price": 1100, "GST": 18, "Quantity": 1},
    {"Product": "Umbrella", "Unit Price": 200, "GST": 12, "Quantity": 4},
    {"Product": "Cigarette", "Unit Price": 100, "GST": 28, "Quantity": 3},
    {"Product": "Honey", "Unit Price": 900, "GST": 0, "Quantity": 2},
]
max_gst_product = max(basket, key=lambda x: (x["Unit Price"] * x["GST"] / 100) * x["Quantity"])
print("Product with maximum GST amount:", max_gst_product["Product"])
total_amount = 0

for product in basket:
    unit_price = product["Unit Price"]
    quantity = product["Quantity"]
    gst_percentage = product["GST"]

    # Calculate the total amount for the product including GST
    total_amount += (unit_price * (1 + gst_percentage / 100)) * quantity

    # Apply a 5% discount for products with a unit price of Rs. 500 or more
    if unit_price >= 500:
        total_amount -= (unit_price * 0.05) * quantity

print("Total amount to be paid to the shopkeeper: Rs.", round(total_amount, 2))
