class TalksRepository:
    def __init__(self):
        self.talks = []

    def insert(self, talk):
        self.talks.append(talk)
        return self.talks
