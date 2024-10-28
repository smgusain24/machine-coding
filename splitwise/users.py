class User:

    def __init__(self, _id: int, name: str):
        self._name = name
        self._id = _id

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def __str__(self):
        return f"Name: {self._name}, UserID : {self._id}"


