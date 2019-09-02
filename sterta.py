class Sterta():
    def __init__(self):
        self.tab = []

    def add_ele(self, x):
        self.tab.append(x)

    def rem_ele(self, y):
        self.tab.remove(y)

    def find_ele(self, z):
        if z in self.tab:
            return True
        else:
            return False

    def all_ele(self):
        return self.tab
    

