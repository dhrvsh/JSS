import subprocess

print("Attempting to install CustomTkinter.")
try:
    result = subprocess.run(["pip", "install", "customtkinter"], capture_output=True, text=True, check=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e}")
    print(f"Stderr: {e.stderr}")

print("Attempting to install Google Generative AI Module.")
try:
    result = subprocess.run(["pip", "install", "google.generativeai"], capture_output=True, text=True, check=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e}")
    print(f"Stderr: {e.stderr}")