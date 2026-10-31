

class_fees = {
    1: ("Sleeper", 40),
    2: ("AC 3 Tier", 100),
    3: ("AC 2 Tier", 150),
    4: ("AC 1 Tier", 200)
}



def calculate_basic_fare(distance):

    fare = 0

   
    fare += min(distance, 100) * 1.50

    
    if distance > 100:
        fare += min(distance - 100, 200) * 1.20

    
    if distance > 300:
        fare += min(distance - 300, 200) * 1.00

    
    if distance > 500:
        fare += (distance - 500) * 0.80

    return fare



def calculate_concession(age):

    if age < 5:
        return 100

    elif age < 12:
        return 50

    elif age >= 60:
        return 10

    else:
        return 0



def calculate_penalty(hours):

    if hours > 48:
        return 10

    elif hours >= 12:
        return 25

    else:
        return 50



print("===== RAILWAY FARE AND RESERVATION SYSTEM =====")

try:

   
    distance = float(input("Enter travel distance (km): "))
    passengers = int(input("Enter number of passengers: "))

    if distance <= 0 or passengers <= 0:
        print("Invalid distance or passenger count!")

    else:

        passenger_details = []
        total_amount = 0

        for i in range(passengers):

            print("\nPassenger", i + 1)

            name = input("Enter passenger name: ")
            age = int(input("Enter passenger age: "))

            if age < 0:
                print("Invalid age!")
                continue

            print("\nTravel Classes:")
            print("1. Sleeper")
            print("2. AC 3 Tier")
            print("3. AC 2 Tier")
            print("4. AC 1 Tier")

            choice = int(input("Select travel class: "))

            if choice not in class_fees:
                print("Invalid class selection!")
                continue

           
            class_name, reservation_fee = class_fees[choice]

            
            basic_fare = calculate_basic_fare(distance)

           
            concession_rate = calculate_concession(age)

            concession = (
                basic_fare * concession_rate / 100
            )

           
            final_fare = (
                basic_fare
                - concession
                + reservation_fee
            )

            
            passenger_details.append({
                "name": name,
                "age": age,
                "class": class_name,
                "basic": basic_fare,
                "concession": concession,
                "reservation": reservation_fee,
                "fare": final_fare
            })

            total_amount += final_fare

        
        print("\n========== RAILWAY FARE RECEIPT ==========")

        for p in passenger_details:

            print("\nPassenger Name:", p["name"])
            print("Age:", p["age"])
            print("Travel Class:", p["class"])
            print("Basic Fare: Rs.", round(p["basic"], 2))
            print("Concession: Rs.", round(p["concession"], 2))
            print("Reservation Fee: Rs.", p["reservation"])
            print("Final Fare: Rs.", round(p["fare"], 2))

        print("\n------------------------------------------")
        print("Total Passengers:", len(passenger_details))
        print("Total Reservation Amount: Rs.",
              round(total_amount, 2))

       
        if passenger_details:

            cancel = input(
                "\nDo you want to cancel the reservation? (yes/no): "
            ).lower()

            if cancel == "yes":

                hours = float(input(
                    "Enter hours before departure: "
                ))

                if hours < 0:
                    print("Invalid cancellation time!")

                else:

                    penalty_rate = calculate_penalty(hours)

                    penalty = (
                        total_amount * penalty_rate / 100
                    )

                    refund = total_amount - penalty

                    print("\n===== CANCELLATION DETAILS =====")
                    print("Cancellation Penalty:",
                          penalty_rate, "%")

                    print("Penalty Amount: Rs.",
                          round(penalty, 2))

                    print("Refund Amount: Rs.",
                          round(refund, 2))

            elif cancel != "no":
                print("Invalid cancellation choice!")

        print("\nRailway Calculation Completed.")

except ValueError:
    print("Invalid input! Please enter the correct data type.")

