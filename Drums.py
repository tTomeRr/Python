import Instrument


class Drums(Instrument.Insturment):
    def __init__(self, drums_type, company, price):
        super().__init__(company, price)
        while drums_type not in ["7-piece", "9-piece", "11-piece"]:
            drums_type = input("Type must be 7-piece, 9-piece or 11-piece: ")
        self.drums_type = drums_type

    def get_type(self):
        return self.drums_type

    def __str__(self):
        return f"Drums: id: {self.id} | type: {self.drums_type} | company: {self.company} | price: {self.price}$"
