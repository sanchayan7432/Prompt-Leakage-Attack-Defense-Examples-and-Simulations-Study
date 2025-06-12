# defense_module.py
class SecureAIAssistant:
    def __init__(self, system_prompt):
        self.system_prompt = system_prompt

    def enforce_policy(self, user_input):
        if any(keyword in user_input.lower() for keyword in ["bypass", "jailbreak", "ignore"]):
            return "I'm sorry, but I can't help with that request."
        return "Processing..."
