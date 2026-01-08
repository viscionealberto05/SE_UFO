from dataclasses import dataclass
@dataclass
class Avvistamento:
    id : int
    s_datetime : str
    city : str
    state : str
    country: str
    shape: str
    duration : int
    duration_hm: str
    comments: str
    date_posted: str
    latitude: str
    longitude: str

    def __str__(self):
        return f"Avvistamento {self.id}, {self.city}, {self.state}, {self.s_datetime}"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)