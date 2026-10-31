

def calculate_concession(category):

    concessions = {
        "general": 0,
        "senior": 10,
        "bpl": 20,
        "insurance": 15
    }

    return concessions[category]



def classify_patient(amount):

    if amount < 1000:
        return "Low-cost Patient"

    elif amount <= 5000:
        return "Medium-cost Patient"

    else:
        return "High-cost Patient"



print("===== HOSPITAL BILLING SYSTEM =====")


name = input("Enter patient name: ")
age = int(input("Enter patient age: "))


if age <= 0:
    print("Invalid age!")
    exit()


print("\nPatient Categories:")
print("1. General")
print("2. Senior Citizen")
print("3. BPL")
print("4. Insurance")

choice = int(input("Enter category choice: "))

categories = {
    1: "general",
    2: "senior",
    3: "bpl",
    4: "insurance"
}

if choice not in categories:
    print("Invalid patient category!")
    exit()

category = categories[choice]


if category == "senior" and age < 60:
    print("Senior citizen concession not applicable!")
    exit()

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))


if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid billing! Charges cannot be negative.")
    exit()


total_bill = consultation + diagnostic + treatment


rate = calculate_concession(category)

concession = total_bill * rate / 100


final_bill = total_bill - concession


classification = classify_patient(final_bill)


print("\n===== HOSPITAL BILL RECEIPT =====")

print("Patient Name:", name)
print("Patient Age:", age)
print("Patient Category:", category.capitalize())

print("\nConsultation Charges: Rs.", consultation)
print("Diagnostic Charges: Rs.", diagnostic)
print("Treatment Charges: Rs.", treatment)

print("---------------------------------")
print("Total Bill: Rs.", round(total_bill, 2))
print("Concession Rate:", rate, "%")
print("Concession Amount: Rs.", round(concession, 2))
print("Final Payable Amount: Rs.", round(final_bill, 2))

print("---------------------------------")
print("Patient Classification:", classification)

print("\nThank you for choosing our hospital!")

