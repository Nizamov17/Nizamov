from collections import deque
class Queue:
    def __init__(self):
        self.inside = deque()
    def add(self, name):
        self.inside.append(name)
    def take_out(self):
        if self.inside:
            return self.inside.popleft()
        else:
            print("Queue is already empty")
    def __str__(self):
        return "=>".join(self.inside)
    def __add__(self, name):
        self.add(name)
        return self
    def __sub__(self, name):
        self.take_out(name)
        return self
    def __iadd__(self, name):
        self.add(name)
        return self
    def __isub__(self, name):
        self.take_out(name)
        return self