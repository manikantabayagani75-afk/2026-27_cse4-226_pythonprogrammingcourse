

total_amount = 0
valid_records = 0
invalid_records = 0

n = int(input("Enter number of invoice records: "))

print("\nEnter invoice records in the format:")
print("ProductCode,Quantity,Amount")

for i in range(n):

    record = input("\nEnter invoice record: ")

   
    fields = record.split(",")


    if len(fields) != 3:
        print("Malformed Record: Incorrect number of fields")
        invalid_records += 1
        continue

    code = fields[0].strip()
    quantity = fields[1].strip()
    amount = fields[2].strip()


    if code == "":
        print("Malformed Record: Missing product code")
        invalid_records += 1
        continue

    
    try:
        qty = int(quantity)
        price = float(amount)

        if qty <= 0 or price <= 0:
            print("Malformed Record: Invalid quantity or amount")
            invalid_records += 1
            continue

      
        print("\nValid Invoice Record")
        print("Product Code:", code)
        print("Quantity:", qty)
        print("Amount: Rs.", price)

        total_amount += price
        valid_records += 1

    except ValueError:
        print("Malformed Record: Invalid numeric values")
        invalid_records += 1


print("\n========== INVOICE SUMMARY ==========")
print("Valid Records:", valid_records)
print("Malformed Records:", invalid_records)
print("Total Invoice Amount: Rs.", total_amount)
print("=====================================")

