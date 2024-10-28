from users import User


class Balance:
    def __init__(self, user1: User, user2: User, amount_owed: float = 0.0):

        self._user1 = user1
        self._user2 = user2
        self._amount_owed = amount_owed

    def get_user1(self):
        return self._user1

    def set_user1(self, user):
        self._user1 = user

    def get_user2(self):
        return self._user2

    def set_user2(self, user):
        self._user2 = user

    def get_amount_owed(self):
        return self._amount_owed

    def set_amount_owed(self, amount):
        self._amount_owed = amount

    def update_balance(self, amount):
        """
        Updates the amount owed. Positive values mean User1 owes User2,
        and negative values mean User2 owes User1.
        """
        self.set_amount_owed(self.get_amount_owed() + amount)

    def get_balance_summary(self):
        """
        Returns a string indicating who owes whom and how much.
        E.g., 'User 1 owes User 2 $50.00' or 'User 2 owes User 1 $25.00'
        """
        if self.get_amount_owed() > 0:
            msg = f"{self.get_user1().get_name()} owes {self.get_user2().get_name()} ${self.get_amount_owed():.2f}"
        elif self.get_amount_owed() < 0:
            msg = f"{self.get_user2().get_name()} owes {self.get_user1().get_name()} ${self.get_amount_owed():.2f}"
        else:
            msg = f"No outstanding balance between {self.get_user1().get_name()} and {self.get_user2().get_name()}"

        return msg

    def __str__(self):
        return self.get_balance_summary()
