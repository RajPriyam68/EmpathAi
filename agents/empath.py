from agents.memory import MemoryBank
from agents.observability import logger

class EmpathAgent:
    def __init__(self):
        self.mb = MemoryBank()

    def generate_reply(self, message, mood_hint=None):
        # simple template reply. replace with LLM call.
        if mood_hint == 'negative':
            reply = "I'm really sorry you're going through this. Would you like a grounding exercise or to talk more?"
        elif mood_hint == 'positive':
            reply = "That's wonderful to hear — tell me more about what's going well!"
        else:
            reply = "Thanks for sharing — I'm here to listen. Tell me more when you're ready."
        # save brief note to memory
        self.mb.write({"msg": message, "mood": mood_hint})
        return reply
