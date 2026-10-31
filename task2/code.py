

def calculate_energy_charge(units):

    if units <= 100:
        charge = units * 2

    elif units <= 200:
        charge = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        charge = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        charge = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    return charge


FIXED_CHARGE = 50
SURCHARGE_RATE = 0.05
REBATE_RATE = 0.10

bills = []


n = int(input("Enter number of months: "))

for i in range(n):

    print("\nMonth", i + 1)

    units = float(input("Enter electricity units consumed: "))

    if units < 0:
        print("Invalid units!")
        continue

   
    energy_charge = calculate_energy_charge(units)

   
    surcharge = energy_charge * SURCHARGE_RATE

     energy_charge = calculate_energy_charge(units)

        rebate = energy_charge * REBATE_RATE
    else:
        rebate = 0

   
    total_bill = (
        energy_charge
        + FIXED_CHARGE
        + surcharge
        - rebate
    )

    bills.append(total_bill)

    print("Energy Charge: Rs.", round(energy_charge, 2))
    print("Fixed Charge: Rs.", FIXED_CHARGE)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Final Bill: Rs.", round(total_bill, 2))

   
    if len(bills) > 1:

        previous_bill = bills[-2]

        increase = (
            (total_bill - previous_bill)
            / previous_bill
        ) * 100

        print("Bill Change:", round(increase, 2), "%")

        if increase > 30:
            print("WARNING: Unusual increase detected!")

        elif increase < 0:
            print("Electricity bill decreased.")

        else:
            print("Normal bill variation.")


print("\n----- MONTHLY BILL SUMMARY -----")

for i, bill in enumerate(bills):
    print("Month", i + 1, ": Rs.", round(bill, 2))

if bills:
    print("Total Bill: Rs.", round(sum(bills), 2))
    print("Average Bill: Rs.", round(sum(bills) / len(bills), 2))

print("\nBilling Process Completed.")

