from splitwise.balance import Balance
from splitwise.enums import SplitType
from splitwise.expense import Expense
from splitwise.users import User


class SplitwiseService:

    def __init__(self):
        self._users = {}
        self._expenses = []
        self._balances = {}

    def get_users(self):
        return self._users

    def add_user(self, user: User):
        self._users[user.get_id()] = user

    def get_expenses(self):
        return self._expenses

    def extend_expenses(self, expenses: list):
        self._expenses.extend(expenses)

    def get_balances(self):
        return self._balances

    def get_balance_by_key(self, key) -> Balance:
        return self._balances[key]

    def delete_balance_by_key(self, key):
        del self._balances[key]

    def set_balance(self, balances: dict):
        self._balances.update(balances)

    def add_expense(self, title: str,
                    amount: float,
                    payer: User,
                    participants: list[User],
                    split_type: SplitType,
                    split_details: dict = None
    ):
        expense = Expense(
            _id=str(len(self._expenses) + 1),
            title=title,
            amount=amount,
            payer=payer,
            participants=participants,
            split_type=split_type.value,
            split_details=split_details
        )
        expense.calculate_split()
        self.extend_expenses([expense])

        self.update_balance(expense)

    def update_balance(self, expense: Expense):
        payer = expense.get_payer()
        for participant, amount_owed in expense.get_split_details().items():
            if participant == payer:
                # Do not consider the payer here
                continue

            # Two-way key for transaction between payer and participant
            balance_key = (participant, payer)
            reverse_balance_key = (payer, participant)

            if balance_key in self.get_balances():
                new_amount = self.get_balance_by_key(balance_key).get_amount_owed() + amount_owed
                self.get_balance_by_key(balance_key).set_amount_owed(new_amount)

            elif reverse_balance_key in self.get_balances():
                # In case payer already owes the participant, this is reduced
                current_reverse_balance = self.get_balance_by_key(reverse_balance_key).get_amount_owed()
                if current_reverse_balance > amount_owed:
                    new_amount = self.get_balance_by_key(reverse_balance_key).get_amount_owed() - amount_owed
                    self.get_balance_by_key(current_reverse_balance).set_amount_owed(new_amount)
                else:
                    # Now participant owes the payer, new balance is created in correct direction
                    balance = Balance(
                        user1=participant,
                        user2=payer,
                        amount_owed=amount_owed-current_reverse_balance
                    )
                    self.set_balance({
                        balance_key: balance
                    })

                    self.delete_balance_by_key(reverse_balance_key)

            else:
                balance = Balance(
                    user1=participant,
                    user2=payer,
                    amount_owed=amount_owed
                )
                self.set_balance({
                    balance_key: balance
                })


    def display_balances(self):
        """Displays all outstanding balances in the system."""
        if not self.get_balances().values():
            print("No outstanding balance")
        for balance in self.get_balances().values():
            print(balance.get_balance_summary())



