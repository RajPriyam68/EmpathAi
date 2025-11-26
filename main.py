import time
from datetime import datetime

class EmpathAI:
    def __init__(self):
        self.session_memory = []
        self.long_term_memory = []
        self.user_profile = {"mood": None, "stress_level": None}

    # ---- Logging Helper ----
    def log(self, event, data=""):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[LOG {timestamp}] {event}: {data}")

    # ---- Memory Functions ----
    def add_to_session_memory(self, text):
        self.session_memory.append(text)
        self.log("Session Memory Updated", text)

    def add_to_long_term_memory(self, text):
        self.long_term_memory.append(text)
        self.log("Long-Term Memory Updated", text)

    # ---- Agent Response ----
    def analyze_message(self, message):
        message_lower = message.lower()

        if any(word in message_lower for word in ["sad", "down", "upset", "depressed"]):
            self.user_profile["mood"] = "sad"
            return "I'm really sorry you're feeling this way. Do you want to talk about what happened?"

        elif any(word in message_lower for word in ["anxious", "stress", "scared", "panic"]):
            self.user_profile["stress_level"] = "high"
            return "It sounds like you're under a lot of pressure. Let's take a deep breath together. I'm here with you."

        elif "happy" in message_lower:
            self.user_profile["mood"] = "happy"
            return "That's amazing! I’m really glad to hear you're feeling good today."

        else:
            return "Thank you for sharing that. Tell me more — I'm listening."

    # ---- Main Chat Loop ----
    def chat(self):
        print("💬 EmpathAI Mental Health Companion")
        print("Type 'exit' to end the session.\n")

        while True:
            user_input = input("You: ")

            if user_input.lower() == "exit":
                print("\nEnding session. Take care of yourself 💛")
                break

            # store in session memory
            self.add_to_session_memory(user_input)

            # analyze message
            response = self.analyze_message(user_input)
            print("EmpathAI:", response)

            # store important emotional cues
            if "sorry you're feeling" in response.lower():
                self.add_to_long_term_memory("User expressed sadness")
            if "pressure" in response.lower():
                self.add_to_long_term_memory("User showed anxiety")

            time.sleep(0.5)


if __name__ == "__main__":
    agent = EmpathAI()
    agent.chat()
