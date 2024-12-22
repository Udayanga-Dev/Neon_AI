import random

class SimpleAI:
    def __init__(self):
        self.responses = [
            "Hello! How can I help you today?",
            "I'm here to assist you.",
            "What can I do for you?",
            "How can I be of service?",
            "Hi there! Need any help?"
        ]

    def get_response(self):
        return random.choice(self.responses)

if __name__ == "__main__":
    ai = SimpleAI()
    print(ai.get_response())