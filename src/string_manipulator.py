class StringManipulator:
    def __init__(self, txt):
        self.splits = [(txt[:i],txt[i:]) for i in range(len(txt) + 1)]
        self.alphbet = sorted('ابتةثجحخدذرزسشصضطظعغفقكلمنهويءآأؤإئ')

    def get_deletes(self):
        deletes = [l + r[1:] for l, r in self.splits if r]
        return deletes
    
    def get_switches(self):
        switches = [l[:-1] + r[0] + l[-1] + r[1:] for l, r in self.splits if r and l]
        return switches
    
    def get_replaces(self):
        replaces = [l + char + r[1:] for l, r in self.splits if r for char in self.alphbet]
        return replaces
    
    def get_inserts(self):
        inserts = [l + char + r for l, r in self.splits for char in self.alphbet]
        return inserts