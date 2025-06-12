# attack/prompt_injection_attack.py
class PromptInjectionAttacker:
    def __init__(self, shadow_model):
        self.shadow_model = shadow_model

    def generate_prompt(self):
        return self.shadow_model.simulate_injection()