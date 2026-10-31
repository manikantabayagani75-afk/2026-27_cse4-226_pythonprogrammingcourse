

def calculate_deduction(salary):

    deduction = 0

    if salary > 10000:
        deduction += min(salary - 10000, 10000) * 0.05

    if salary > 20000:
        deduction += min(salary - 20000, 20000) * 0.10

    if salary > 40000:
        deduction += (salary - 40000) * 0.15

    return deduction



print("===== EMPLOYEE PAYROLL SYSTEM =====")


emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")


basic = float(input("Enter Basic Salary: Rs. "))
overtime_hours = float(input("Enter Overtime Hours: "))
incentive = float(input("Enter Incentive Amount: Rs. "))


if basic < 0 or overtime_hours < 0 or incentive < 0:
    print("Invalid Input! Values cannot be negative.")

else:

   
    hra = basic * 0.20
    da = basic * 0.10


    overtime_pay = overtime_hours * 200


    gross_salary = (
        basic + hra + da + overtime_pay + incentive
    )

    
    deduction = calculate_deduction(gross_salary)


    net_salary = gross_salary - deduction


    print("\n========================================")
    print("         EMPLOYEE SALARY STATEMENT")
    print("========================================")

    print("Employee ID       :", emp_id)
    print("Employee Name     :", name)

    print("----------------------------------------")
    print("Basic Salary      : Rs.", round(basic, 2))
    print("HRA (20%)         : Rs.", round(hra, 2))
    print("DA (10%)          : Rs.", round(da, 2))
    print("Overtime Payment  : Rs.", round(overtime_pay, 2))
    print("Incentives        : Rs.", round(incentive, 2))

    print("----------------------------------------")
    print("Gross Salary      : Rs.", round(gross_salary, 2))
    print("Total Deductions  : Rs.", round(deduction, 2))
    print("----------------------------------------")
    print("NET SALARY        : Rs.", round(net_salary, 2))
    print("========================================")

    print("Payroll Calculation Completed.")

