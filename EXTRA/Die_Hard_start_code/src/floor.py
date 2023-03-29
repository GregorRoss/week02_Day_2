class Floor:
    def __init__(self):
        self.people = []

    def floor_count(self):
        return len(self.people)
    
    def add_person(self, bad_person):
        self.people.append(bad_person)

    def remove_person(self, bad_person):
        self.people.remove(bad_person)
    