from splitwise.enums import SplitType
from splitwise.service import SplitwiseService
from splitwise.users import User


def main():
    splitwise = SplitwiseService()

    while True:
        try:
            num_users = int(input("Enter number of users "))
            break
        except ValueError:
            print("Invalid Input")

    for i in range(1, num_users+1):
        name = input("Enter user name: ")
        user = User(_id=i, name = name)
        splitwise.add_user(user)

    while True:
        print("\n1. Add Expense")
        print("2. Display Balances")
        print("3. Exit")

        choice = input("Choose an option: ")

        if int(choice) == 1:
            title = input("Enter title of expense: ")
            try:
                amount = float(input("Enter total expense amount: "))
            except ValueError:
                print("Invalid input ")
                continue

            payer_id = int(input("Enter the ID of the payer: "))
            payer = splitwise.get_users().get(payer_id)
            if not payer:
                print("Payer ID not found.")
                continue

            participant_ids = input("Enter participant IDs separated by spaces: ").split()
            participants = [splitwise.get_users().get(int(pid)) for pid in participant_ids]
            if None in participants:
                print("One or more participant IDs were not found.")
                continue

            print("\nChoose Split Type:")
            print("1. Equal")
            print("2. Exact")
            print("3. Percent")

            split_type_choice = input("Enter the split type: ")

            if split_type_choice == "1":
                split_type = SplitType.EQUAL
                split_details = None

            elif split_type_choice == "2":
                split_type = SplitType.EXACT
                split_details = {}
                for participant in participants:
                    try:
                        exact_amount = float(input(f"Enter exact amount for {participant.get_name()}: "))
                        split_details[participant] = exact_amount
                    except ValueError:
                        print("Invalid amount. Please enter a number.")
                        break
                if sum(split_details.values()) != amount:
                    print("Error: Exact amounts do not sum up to the total amount.")
                    continue

            elif split_type_choice == "3":
                split_type = SplitType.PERCENT
                split_details = {}
                for participant in participants:
                    try:
                        percentage = float(input(f"Enter percentage for {participant.get_name()}: "))
                        split_details[participant] = percentage
                    except ValueError:
                        print("Invalid percentage. Please enter a number.")
                        break
                if sum(split_details.values()) != 100:
                    print("Error: Percentages do not sum up to 100.")
                    continue

            else:
                print("Invalid split type choice.")
                continue

            # Add the expense to Splitwise
            splitwise.add_expense(
                title=title,
                amount=amount,
                payer=payer,
                participants=participants,
                split_type=split_type,
                split_details=split_details
            )
            print(f"Expense '{title}' added successfully.")

        elif int(choice) == 2:
            print("\nOutstanding Balances:")
            splitwise.display_balances()

        elif int(choice) == 3:
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
