class Session:
    def __init__(self, setsPerSession=1, restBetweenSets=0, takesPerSet=5, hangsPerTake=6, restBetweenTakes=2, hangtime=7, resttime=3):
        self.setsPerSession = setsPerSession
        self.restBetweenSets = restBetweenSets
        self.takesPerSet = takesPerSet
        self.hangsPerTake = hangsPerTake
        self.restBetweenTakes = restBetweenTakes
        self.hangtime = hangtime
        self.resttime = resttime

    def set_setsPerSession(self, setsPerSession):
        self.setsPerSession = setsPerSession
    def set_restBetweenSets(self, restBetweenSets):
        self.restBetweenSets = restBetweenSets
    def set_takesPerSet(self, takesPerSet):
        self.takesPerSet = takesPerSet
    def set_hangsPerTake(self, hangsPerTake):
        self.hangsPerTake = hangsPerTake
    def set_restBetweenTakes(self, restBetweenTakes):
        self.restBetweenTakes = restBetweenTakes
    def set_hangtime(self, hangtime):
        self.hangtime = hangtime
    def set_resttime(self, resttime):
        self.resttime = resttime

class Set:
    def __init__(self, restBetweenSets=5, takesPerSet=5, restBetweenTakes=2, hangsPerTake=6, hangtime=7, resttime=3):
        self.restBetweenSets = restBetweenSets
        self.takesPerSet = takesPerSet
        self.hangsPerTake = hangsPerTake
        self.restBetweenTakes = restBetweenTakes
        self.hangtime = hangtime
        self.resttime = resttime

    def set_restBetweenSets(self, restBetweenSets):
        self.restBetweenSets = restBetweenSets
    def set_takesPerSet(self, takesPerSet):
        self.takesPerSet = takesPerSet
    def set_hangsPerTake(self, hangsPerTake):
        self.hangsPerTake = hangsPerTake
    def set_restBetweenTakes(self, restBetweenTakes):
        self.restBetweenTakes = restBetweenTakes
    def set_hangtime(self, hangtime):
        self.hangtime = hangtime
    def set_resttime(self, resttime):
        self.resttime = resttime

class Take:
    def __init__(self, hangsPerTake=6, restBetweenTakes=2, hangtime=7, resttime=3):
        self.hangsPerTake = hangsPerTake
        self.restBetweenTakes = restBetweenTakes
        self.hangtime = hangtime
        self.resttime = resttime

    def set_hangsPerTake(self, hangsPerTake):
        self.hangsPerTake = hangsPerTake
    def set_restBetweenTakes(self, restBetweenTakes):
        self.restBetweenTakes = restBetweenTakes
    def set_hangtime(self, hangtime):
        self.hangtime = hangtime
    def set_resttime(self, resttime):
        self.resttime = resttime
