 #  Simple in memory store for agent state, past actions, or results.

class Memory:
    def __init__(self):
        self.store = []

    def add(self, item):
        self.store.append(item)

    def get_all(self):
        return self.store

    def clear(self):
        self.store = []
