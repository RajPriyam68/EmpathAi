import time
class MemoryBank:
    def __init__(self):
        self.session = []
        self.long_term = []

    def write(self, item: dict):
        item['ts'] = time.time()
        self.session.append(item)
        # simple long-term heuristic: store negative mentions
        if item.get('mood') == 'negative':
            self.long_term.append(item)

    def read_session(self, last_n=20):
        return self.session[-last_n:]

    def read_long_term(self, last_n=50):
        return self.long_term[-last_n:]
