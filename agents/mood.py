class MoodAgent:
    NEGATIVE = ['sad','down','depressed','anxious','stress','panic','lonely']
    POSITIVE = ['happy','great','good','excited','joy']

    def detect(self, text: str):
        t = text.lower()
        neg = any(w in t for w in self.NEGATIVE)
        pos = any(w in t for w in self.POSITIVE)
        if neg:
            return 'negative'
        if pos:
            return 'positive'
        return 'neutral'
