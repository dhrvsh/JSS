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


print("Attempting to install FontTools.")
try:
    result = subprocess.run(["pip", "install", "fonttools"], capture_output=True, text=True, check=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e}")
    print(f"Stderr: {e.stderr}")

# from fontTools.ttLib import TTFont
# font = TTFont('SFPRODISPLAYREGULAR.OTF')
# font.save(font)

import shutil
import os

source_font_path = "SFPRODISPLAYREGULAR.OTF"  # Replace with the actual path to your font file
destination_font_directory = "C:\\Windows\\Fonts" # Or appropriate directory for your OS

# Ensure the destination directory exists
if not os.path.exists(destination_font_directory):
    os.makedirs(destination_font_directory)

shutil.copy(source_font_path, destination_font_directory)
print(f"Font copied to: {destination_font_directory}")