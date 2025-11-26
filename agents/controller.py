from agents.empath import EmpathAgent
from agents.mood import MoodAgent
from agents.safety import SafetyAgent
from agents.observability import logger, tracer, metrics

class Controller:
    def __init__(self):
        self.empath = EmpathAgent()
        self.mood = MoodAgent()
        self.safety = SafetyAgent()

    def run(self):
        print("=== EmpathAI Enhanced ===")
        print("Type 'exit' to quit.\n")
        while True:
            text = input("You: ").strip()
            if text.lower() in ('exit','quit'):
                print("Goodbye — take care.")
                break
            trace_id = tracer.start_trace('conversation')
            logger.log_event('message_received', {'text': text, 'trace': trace_id})
            # safety first
            risk = self.safety.check(text)
            if risk.get('risk_flag'):
                logger.log_event('escalation', {'trace': trace_id, 'risk': risk})
                print("EmpathAI: I'm concerned about your safety. I've provided resources and notified a human moderator.")
                tracer.end_trace(trace_id)
                continue
            # mood detection and response
            mood = self.mood.detect(text)
            reply = self.empath.generate_reply(text, mood)
            print("EmpathAI:", reply)
            metrics.increment_messages()
            tracer.end_trace(trace_id)
