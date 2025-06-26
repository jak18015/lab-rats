import os
from modules import ab_dilutions, c1v1

if not os.getcwd().endswith("lab-calculations"):
    raise RuntimeError("Please run this script from the 'lab-calculations' directory.")

scripts = {
    'ab_dilutions': ab_dilutions.calculate_ab_dilutions,
    'c1v1': c1v1.c1v1_calculator,
    }

script_choices = list(scripts.keys())
print("Available scripts:")
for i, script_name in enumerate(script_choices, start=1):
    print(f"\t{i}. {script_name}")

script = input("Enter the number nextto the script to run (e.g., 1 for 'ab_dilutions'): ").strip()
print(script)
if script.isdigit() and 1 <= int(script) <= len(script_choices):
    script_name = script_choices[int(script) - 1]
    print(f"Running {script_name}...")
    scripts[script_name]()
else:
    print("Invalid input. Please enter a valid number corresponding to the script you want to run.")
    exit(1)