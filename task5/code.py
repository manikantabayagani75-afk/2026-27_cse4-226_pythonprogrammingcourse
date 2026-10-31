

plans = [
    {
        "name": "Plan A",
        "price": 199,
        "data": 2,
        "calls": 200,
        "validity": 28
    },
    {
        "name": "Plan B",
        "price": 299,
        "data": 5,
        "calls": 500,
        "validity": 28
    },
    {
        "name": "Plan C",
        "price": 399,
        "data": 10,
        "calls": 1000,
        "validity": 56
    },
    {
        "name": "Plan D",
        "price": 499,
        "data": 15,
        "calls": 1500,
        "validity": 84
    }
]


DATA_RATE = 20
CALL_RATE = 1

print("===== TELECOM PLAN OPTIMIZATION =====")


data_usage = float(input("Enter data usage (GB): "))
call_usage = float(input("Enter call usage (minutes): "))
required_validity = int(input("Enter required validity (days): "))
budget = float(input("Enter maximum budget (Rs.): "))

 call_usage < 0
        or required_validity <= 0 or budget < 0):

    print("Invalid input! Enter valid non-negative values.")

else:

    eligible_plans = []

    print("\n========== PLAN COMPARISON ==========")

    for plan in plans:

        
        excess_data = max(0, data_usage - plan["data"])

       
        excess_calls = max(0, call_usage - plan["calls"])

       
        data_charge = excess_data * DATA_RATE
        call_charge = excess_calls * CALL_RATE

        
        total_cost = (
            plan["price"] + data_charge + call_charge
        )

        
        if (total_cost <= budget and
                plan["validity"] >= required_validity):

            status = "Eligible"

            eligible_plans.append({
                "name": plan["name"],
                "cost": total_cost,
                "validity": plan["validity"]
            })

        else:
            status = "Not Eligible"

       
        print("\nPlan:", plan["name"])
        print("Base Price: Rs.", plan["price"])
        print("Excess Data Charge: Rs.", data_charge)
        print("Excess Call Charge: Rs.", call_charge)
        print("Total Cost: Rs.", round(total_cost, 2))
        print("Validity:", plan["validity"], "days")
        print("Status:", status)

    
    print("\n========== FINAL RESULT ==========")

    if eligible_plans:

        best_plan = min(
            eligible_plans,
            key=lambda x: x["cost"]
        )

        print("Most Economical Plan:",
              best_plan["name"])

        print("Total Cost: Rs.",
              round(best_plan["cost"], 2))

        print("Validity:",
              best_plan["validity"], "days")

        print("\nAll Eligible Plans:")

        for plan in eligible_plans:
            print(
                plan["name"],
                "- Rs.",
                round(plan["cost"], 2)
            )

    else:
        print("No eligible mobile plans found.")
        print("Consider increasing your budget or")
        print("reducing your usage or validity requirement.")

    print("\nOptimization Completed.")

