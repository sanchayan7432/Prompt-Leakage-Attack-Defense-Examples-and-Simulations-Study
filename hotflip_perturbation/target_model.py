# target_model.py
class TargetLLM:
    def __init__(self, system_prompt):
        self.system_prompt = system_prompt

    def query(self, prompt):
        # Simulate leaking prompt if jailbreak is semi-successful
        if "ignore previous" in prompt.lower():
            return self.system_prompt[:200] + "..."
        return "I'm sorry, but I can't help with that request."
