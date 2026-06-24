class Metrics:
    def __init__(self):
        self.counters = {}

    def increment(self, name: str, value: int = 1):
        if name not in self.counters:
            self.counters[name] = 0
        self.counters[name] += value

    def get(self, name: str) -> int:
        return self.counters.get(name, 0)