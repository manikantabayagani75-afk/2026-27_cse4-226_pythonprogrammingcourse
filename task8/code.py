


balance = float(input("Enter initial balance: Rs. "))

total_deposits = 0
total_withdrawals = 0
successful = 0
rejected = 0

withdrawal_limit = 10000

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\nTransaction", i + 1)
    print("1. Deposit")
    print("2. Withdraw")

    choice = input("Enter transaction type (D/W): ").upper()
    amount = float(input("Enter amount: Rs. "))

    if amount <= 0:
        print("Rejected: Invalid amount")
        rejected += 1

    elif choice == 'D':
        balance += amount
        total_deposits += amount
        successful += 1
        print("Deposit successful!")

    elif choice == 'W':
        if amount > withdrawal_limit:
            print("Rejected: Withdrawal limit exceeded")
            rejected += 1

        elif amount > balance:
            print("Rejected: Insufficient balance")
            rejected += 1

        else:
            balance -= amount
            total_withdrawals += amount
            successful += 1
            print("Withdrawal successful!")

    else:
        print("Rejected: Invalid transaction type")
        rejected += 1

    print("Current Balance: Rs.", balance)


print("\n========== ATM TRANSACTION SUMMARY ==========")
print("Total Deposits       : Rs.", total_deposits)
print("Total Withdrawals    : Rs.", total_withdrawals)
print("Successful Transactions:", successful)
print("Rejected Transactions  :", rejected)
print("Final Account Balance  : Rs.", balance)
print("============================================")

