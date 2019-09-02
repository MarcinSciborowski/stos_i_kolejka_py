class Stos():
    def __init__(self):
        self.tab = []
    def push(self, el):
        self.tab.append(el)
        return self.tab
    def pop(self):
        if self.is_empty() == True:
            return False
        else:
            el_rem = self.tab[len(self.tab)-1]
            self.tab.remove(self.tab[len(self.tab)-1])
            return el_rem
    def top(self):
        if self.is_empty() == True:
            return False
        return self.tab[len(self.tab)-1]
    def is_empty(self):
        return self.tab == []
    def tablica(self):
        return self.tab


