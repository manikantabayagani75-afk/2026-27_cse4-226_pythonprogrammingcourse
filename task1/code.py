
# University Scholarship Allocation System

MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000
SCHOLARSHIP_QUOTA = 3


def evaluate_applicant(applicant):
    """Return the reasons why an applicant is ineligible."""
    reasons = []

    marks = applicant["marks"]

    if not marks or any(m < 0 or m > 100 for m in marks):
        return ["Invalid or missing subject marks"]

    if not 0 <= applicant["attendance"] <= 100:
        return ["Invalid attendance percentage"]

    if applicant["income"] < 0:
        return ["Invalid family income"]

    aggregate = sum(marks) / len(marks)

    if aggregate < MIN_AGGREGATE:
        reasons.append("Aggregate marks below 75%")

    if any(m < MIN_SUBJECT_MARK for m in marks):
        reasons.append("Subject marks below 60%")

    if applicant["attendance"] < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if applicant["income"] > MAX_INCOME:
        reasons.append("Family income exceeds Rs. 250000")

    return reasons


def allocate_scholarships(applicants, quota):
    eligible = []
    rejected = []

    for student in applicants:
        student["aggregate"] = (
            sum(student["marks"]) / len(student["marks"])
            if student["marks"] else 0
        )

        reasons = evaluate_applicant(student)

        if reasons:
            rejected.append((student, reasons))
        else:
            eligible.append(student)

    
    eligible.sort(
        key=lambda s: (
            -s["aggregate"],
            -sum(s["marks"][:2]),
            -s["attendance"],
            s["income"],
            s["id"]
        )
    )

    winners = eligible[:max(0, quota)]

    return eligible, rejected, winners



applicants = [
    {
        "id": "A101", "name": "Ananya",
        "marks": [90, 85, 88],
        "attendance": 95, "income": 180000
    },
    {
        "id": "A102", "name": "Bharat",
        "marks": [85, 85, 85],
        "attendance": 90, "income": 120000
    },
    {
        "id": "A103", "name": "Charan",
        "marks": [78, 80, 76],
        "attendance": 85, "income": 200000
    },
    {
        "id": "A104", "name": "Divya",
        "marks": [92, 55, 90],
        "attendance": 98, "income": 100000
    },
    {
        "id": "A105", "name": "Esha",
        "marks": [85, 85, 85],
        "attendance": 95, "income": 150000
    }
]

eligible, rejected, winners = allocate_scholarships(
    applicants, SCHOLARSHIP_QUOTA
)

print("UNIVERSITY SCHOLARSHIP ALLOCATION")
print("-" * 60)

print("\nRANKED ELIGIBLE APPLICANTS")
for rank, student in enumerate(eligible, start=1):
    print(
        f"{rank}. {student['id']} - {student['name']} | "
        f"Aggregate: {student['aggregate']:.2f}% | "
        f"Attendance: {student['attendance']}%"
    )

print("\nINELIGIBLE APPLICANTS")
if not rejected:
    print("None")

for student, reasons in rejected:
    print(f"{student['id']} - {student['name']}")
    for reason in reasons:
        print(f"  - {reason}")

print("\nSCHOLARSHIP AWARDEES")
if not winners:
    print("No scholarships awarded")

for rank, student in enumerate(winners, start=1):
    print(
        f"{rank}. {student['id']} - {student['name']} | "
        f"Aggregate: {student['aggregate']:.2f}%"
    )

