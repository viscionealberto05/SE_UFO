from dataclasses import dataclass
@dataclass
class Stato:
    id :str
    name :str
    capital :str
    neighbors :str
    capital:str
    lat:str
    lng:str
    area : int
    population : int
    neighbors:str

    def __str__(self):
        return f"Stato: {self.id},{self.capital}"
    def __repr__(self):
        return f"Stato: {self.id},{self.capital}"
    def __eq__(self, other):
        return self.id == other.id
    def __hash__(self):
        return hash(self.id)
