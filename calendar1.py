class MyCalendar(object):

    def __init__(self):
        self.contain = []

    def book(self, start, end):
        for s, e in self.contain:
            if start < e and end > s:
                return False
        self.contain.append((start, end))
        return True

class 
