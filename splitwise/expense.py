from users import User
from enums import SplitType

class Expense:
    def __init__(
        self,
        _id: str,
        title: str,
        amount: float,
        payer: User,
        participants: list[User],
        split_type: str,
        split_details: dict = None,
    ):
        self._id = _id
        self._title = title
        self._amount = amount
        self._payer = payer
        self._participants = participants
        self._split_type = split_type
        self._split_details = split_details

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_amount(self):
        return self._amount

    def get_payer(self):
        return self._payer

    def get_participants(self):
        return self._participants

    def get_split_type(self):
        return self._split_type

    def get_split_details(self):
        return self._split_details

    def set_split_details(self, details):
        self._split_details = details

    def calculate_split(self):
        """
        Calculate split for an Expense
        """
        if self.get_split_type() == SplitType.EQUAL.value:
            """
            For equal splits, divide total expense in equal parts
            """
            split_amount = self.get_amount() / len(self.get_participants())
            details = {participant: split_amount for participant in self.get_participants()}
            self.set_split_details(details)

        elif self.get_split_type() == SplitType.PERCENT.value:
            """
            For percent splits, calculate percent share 
            """
            total_percent = sum(self.get_split_details().values())
            if total_percent != 100.00:
                raise ValueError("Split Percentages do not match!")

            details = {}
            for participant, percentage in self.get_split_details().items():
                details[participant] = (percentage/100) * self.get_amount()
            self.set_split_details(details)

        elif self.get_split_type() == SplitType.EXACT.value:
            """
            For exact splits, determined by user
            """
            total_amount = sum(self.get_split_details().values())
            if total_amount != self.get_amount():
                raise ValueError("Split amount does not match total amount!")

        else:
            raise ValueError("Unsupported split type provided.")


