class SafetyAgent:
    SIGNALS = ['kill myself','end my life','i want to die','suicide']

    def check(self, text: str):
        t = text.lower()
        flag = any(s in t for s in self.SIGNALS)
        score = 0.95 if flag else 0.0
        return {'risk_score': score, 'risk_flag': flag, 'explain': 'keywords' if flag else 'none'}
