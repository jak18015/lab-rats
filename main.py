import os
from modules import (
    ab, 
    ifa, 
    gibson, 
    date_calculator, 
    week_calculator, 
    lipofectamine
)
from modules.config_functions import load_config, save_config, edit_config

scripts = {
    'ab': ab.calculate_ab_dilutions,
    'ifa': ifa.c1v1_calculator,
    'gibson': gibson.run_gibson_mixture,
    'date_calculator': date_calculator.calculate_hours_between_dates,
    'week_calculator': week_calculator.week_number_calculator,
    'lipofectamine': lipofectamine.run_lipofection_calculator
}
script_choices = list(scripts.keys())

def main():
    """Run the script selected by the user."""
    if not os.getcwd().endswith("lab-rats"):
        raise RuntimeError("Please run this script from the 'lab-rats' directory.")

    print("Available scripts:")
    for i, script_name in enumerate(script_choices, start=1):
        print(f"\t{i}. {script_name}")

    script = input("Enter the number next to the script to run (e.g., 1 for 'ab_dilutions'): ").strip()

    if script.isdigit() and 1 <= int(script) <= len(script_choices):
        script_name = script_choices[int(script) - 1]
        print(f"Running {script_name}...")
        
        # Load config
        config = load_config(script_name)
        if config is None:
            return

        # Edit config
        edit_config(config)

        # Optionally save updated config
        if input("Do you want to save the updated configuration? (y/n): ").strip().lower() == 'y':
            save_config(script_name, config)

        # Run the script with the updated configuration
        scripts[script_name](config)
    else:
        print("Invalid input. Please enter a valid number corresponding to the script you want to run.")
        exit(1)

if __name__ == "__main__":
    main()