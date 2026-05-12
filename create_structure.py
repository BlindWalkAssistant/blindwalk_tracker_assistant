import os

project_name = "blind_walk_assistant"

folders = [
    "configs",
    "models",
    "src",
    "data/test_images",
    "data/sample_video",
    "outputs/predictions",
    "outputs/logs",
    "scripts"
]

files = [
    "README.md",
    "requirements.txt",
    "run.py",
    "configs/config.yaml",
    "src/detector.py",
    "src/tracker.py",
    "src/distance_estimator.py",
    "src/voice_alert.py",
    "src/utils.py",
    "scripts/download_model.py"
]

# create main folder
os.makedirs(project_name, exist_ok=True)

# create folders
for folder in folders:
    os.makedirs(os.path.join(project_name, folder), exist_ok=True)

# create files
for file in files:
    open(os.path.join(project_name, file), 'a').close()

print("✅ Project structure created successfully!")