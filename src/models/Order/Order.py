

class Order:

    def __init__(self, first_name, last_name, address, postcode, suburb):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.postcode = postcode
        self.suburb = suburb

    def json(self):
        return {"first_name": self.first_name,
                "last_name": self.last_name,
                "address": self.address,
                "postcode": self.address,
                "suburb": self.suburb}
