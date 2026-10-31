

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

capacity = int(input("Enter classroom capacity: "))

total_seats = rows * cols


if rows <= 0 or cols <= 0 or capacity <= 0:
    print("Invalid classroom dimensions or capacity.")

elif total_seats > capacity:
    print("Error: Seating exceeds classroom capacity.")

else:
   
    reserved_count = int(input("Enter number of reserved seats: "))

    reserved = set()

    print("Enter reserved seat positions (row column):")

    for i in range(reserved_count):
        r, c = map(int, input().split())

        if 1 <= r <= rows and 1 <= c <= cols:
            reserved.add((r, c))
        else:
            print("Invalid reserved position ignored.")

    print("\nEXAMINATION SEATING ARRANGEMENT")

    available = 0
    reserved_total = 0
    restricted = 0

    
    for i in range(1, rows + 1):

        print("Row", i, ":", end=" ")

        for j in range(1, cols + 1):

            
            if (i, j) in reserved:
                seat = "R"
                reserved_total += 1

           
            elif (i + j) % 2 == 0:
                seat = "X"
                restricted += 1

            else:
                seat = "S"
                available += 1

            print(f"[{i}-{j}:{seat}]", end=" ")

        print()

    
    print("\n========== SEATING SUMMARY ==========")
    print("Total Classroom Seats :", total_seats)
    print("Reserved Seats        :", reserved_total)
    print("Restricted Seats      :", restricted)
    print("Available Seats       :", available)
    print("Classroom Capacity    :", capacity)
    print("=====================================")

