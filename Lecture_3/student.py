class Student:
    __slots__ = ['id', 'name', 'address']

    def __init__(self, id_, name, address):
        self.id = id_
        self.name = name
        self.address = address

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
        }

    @staticmethod
    def from_json(data):
        return Student(
            data["id"],
            data["name"],
            data["address"]
        )
