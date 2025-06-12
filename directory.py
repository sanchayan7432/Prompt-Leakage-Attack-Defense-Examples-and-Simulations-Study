import os

# Create a project folder structure for each attack type
base_dir = "/data1/SANCHAYANghosh01/PLeak_SecAlign"
attack_types = [
    "jailbreak_prompts",
    "prompt_injections",
    "role_playing_attacks",
    "hotflip_perturbation",
    "gradient_guided_insertions"
]
folders = []

for attack in attack_types:
    project_path = os.path.join(base_dir, attack)
    os.makedirs(os.path.join(project_path, "defense"), exist_ok=True)
    os.makedirs(os.path.join(project_path, "attack"), exist_ok=True)
    os.makedirs(os.path.join(project_path, "models"), exist_ok=True)
    os.makedirs(os.path.join(project_path, "evaluation"), exist_ok=True)
    folders.append(project_path)

folders
