

tax_rates = {
    "electronics": 18,
    "clothing": 5,
    "grocery": 0,
    "furniture": 12
}


MAX_DISCOUNT = 2000

def calculate_discount(subtotal):

    if subtotal >= 10000:
        rate = 15

    elif subtotal >= 5000:
        rate = 10

    elif subtotal >= 1000:
        rate = 5

    else:
        rate = 0

    discount = subtotal * rate / 100

   
    discount = min(discount, MAX_DISCOUNT, subtotal)

    return rate, discount



print("===== RETAIL BILLING SYSTEM =====")

customer = input("Enter customer name: ")

n = int(input("Enter number of products: "))

# Validate product count
if n <= 0:
    print("Invalid product count!")

else:

    products = []
    total_subtotal = 0

    
    for i in range(n):

        print("\nProduct", i + 1)

        name = input("Enter product name: ")
        category = input(
            "Enter category (Electronics/Clothing/Grocery/Furniture): "
        ).lower()

        price = float(input("Enter unit price: Rs. "))
        quantity = int(input("Enter quantity: "))

        
        if category not in tax_rates:
            print("Invalid product category!")
            continue

        if price < 0 or quantity <= 0:
            print("Invalid price or quantity!")
            continue

        
        item_total = price * quantity

        total_subtotal += item_total

        products.append({
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity,
            "subtotal": item_total,
            "tax_rate": tax_rates[category]
        })

    if not products:
        print("No valid products entered.")

    else:

       
        discount_rate, discount = calculate_discount(
            total_subtotal
        )

        
        total_tax = 0

        print("\n========== ITEMIZED INVOICE ==========")
        print("Customer Name:", customer)

        print("--------------------------------------")

        for p in products:

            
            item_discount = (
                p["subtotal"] / total_subtotal
            ) * discount

            taxable_amount = (
                p["subtotal"] - item_discount
            )

            
            item_tax = (
                taxable_amount * p["tax_rate"] / 100
            )

            total_tax += item_tax

            print("\nProduct:", p["name"])
            print("Category:", p["category"].capitalize())
            print("Unit Price: Rs.", p["price"])
            print("Quantity:", p["quantity"])
            print("Subtotal: Rs.", round(p["subtotal"], 2))
            print("Discount: Rs.", round(item_discount, 2))
            print("Tax Rate:", p["tax_rate"], "%")
            print("Tax Amount: Rs.", round(item_tax, 2))

       
        taxable_total = total_subtotal - discount

        final_bill = taxable_total + total_tax

        print("\n--------------------------------------")
        print("Total Subtotal: Rs.",
              round(total_subtotal, 2))

        print("Discount Rate:", discount_rate, "%")

        print("Total Discount: Rs.",
              round(discount, 2))

        print("Taxable Amount: Rs.",
              round(taxable_total, 2))

        print("Total Tax: Rs.",
              round(total_tax, 2))

        print("--------------------------------------")
        print("FINAL BILL: Rs.",
              round(final_bill, 2))

        print("======================================")
        print("Thank you for shopping!")

