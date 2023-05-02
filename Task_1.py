class Batary:
    def __init__(self, max_charge=5):
        self.capacity = []
        self.max_charge = max_charge
    def charge(self):
        if len(self.capacity) < self.max_charge:
            self.capacity.append(')')
        else:
            print('Battery is already fully charged')
    def discharge(self):
        if self.capacity:
            self.capacity.pop()
        else:
            print('Battery is already empty')
    def __str__(self):
        return '[' + ''.join(self.capacity) + ']'