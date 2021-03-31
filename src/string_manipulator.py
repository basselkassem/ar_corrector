class StringManipulator:
    def __init__(self, txt = ''):
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
    
    def get_edits1(self, allow_switches = True):
        deletes = self.get_deletes()
        replaces = self.get_replaces()
        inserts = self.get_inserts()
        edits = deletes + replaces + inserts
        if allow_switches:
            edits += self.get_switches()
        return list(set(edits))
    
    def get_edits2(self, allow_switchs = True):
        edits1 = self.get_edits1(allow_switches=allow_switchs)
        edits2 = set()
        for edit1 in edits1:
            manipulator = StringManipulator(edit1)
            for edit2 in manipulator.get_edits1():
                edits2.add(edit2)
        return list(edits2)
        