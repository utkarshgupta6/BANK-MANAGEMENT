from database import create_account
from banking_operations import deposit, withdraw, check_balance

def main():
    print("====================================")
    print("   WELCOME TO BANK MANAGEMENT SYSTEM   ")
    print("====================================")

    while True:
        print("\n1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            acc_num = input("Enter Account Number: ").strip()
            name = input("Enter Account Holder Name: ").strip()
            balance = float(input("Enter Initial Balance: "))
            success, msg = create_account(acc_num, name, balance)
            print(msg)

        elif choice == '2':
            acc_num = input("Enter Account Number: ").strip()
            amt = float(input("Enter Amount to Deposit: "))
            success, msg = deposit(acc_num, amt)
            print(msg)

        elif choice == '3':
            acc_num = input("Enter Account Number: ").strip()
            amt = float(input("Enter Amount to Withdraw: "))
            success, msg = withdraw(acc_num, amt)
            print(msg)

        elif choice == '4':
            acc_num = input("Enter Account Number: ").strip()
            msg = check_balance(acc_num)
            print(msg)

        elif choice == '5':
            print("\nThank you for using Bank Management System!")
            break

        else:
            print("Invalid choice! Please select between 1 and 5.")

if __name__ == "__main__":
    main()
