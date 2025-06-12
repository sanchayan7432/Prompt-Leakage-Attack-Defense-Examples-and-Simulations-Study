# attack/roleplay_attack.py
class RoleplayAttacker:
    def __init__(self, shadow_model):
        self.shadow_model = shadow_model

    def generate_prompt(self):
        return self.shadow_model.simulate_roleplay()
