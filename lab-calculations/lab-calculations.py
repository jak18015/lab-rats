import os
import json
from modules import ab, ifa, gibson, date_calculator, week_calculator

def load_config(script_name):
    config_path = f"configs/{script_name}_config.json"
    if not os.path.exists(config_path):
        print(f"Configuration file for {script_name} not found.")
        return None
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

def save_config(script_name, config):
    config_path = f"configs/{script_name}_config.json"
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)

def edit_config(config):
    def convert_to_type(value, new_value):
        try:
            if isinstance(value, bool):
                return new_value.lower() in ['true', '1', 'yes', 'y']
            if isinstance(value, int):
                return int(new_value)
            if isinstance(value, float):
                return float(new_value)
            return str(new_value)  # Convert to string by default
        except ValueError:
            print(f"Invalid input for {value}, keeping original value.")
            return value

    def prompt_for_value(full_key, current_value):
        new_value = input(f"Enter new value for {full_key} (current: {current_value}, press Enter to keep current): ").strip()
        if new_value:
            return convert_to_type(current_value, new_value)
        return current_value

    def edit_nested_config(prefix, local_config):
        for key, value in local_config.items():
            full_key = f"{prefix}{key}"
            if isinstance(value, dict):
                print(f"\nEditing dictionary for '{full_key}':")
                edit_nested_config(f"{full_key}.", value)
            else:
                local_config[key] = prompt_for_value(full_key, value)

    edit_nested_config("", config)

def main():
    if not os.getcwd().endswith("lab-calculations"):
        raise RuntimeError("Please run this script from the 'lab-calculations' directory.")

    scripts = {
        'ab': ab.calculate_ab_dilutions,
        'ifa': ifa.c1v1_calculator,
        'gibson': gibson.run_gibson_mixture,
        'date_calculator': date_calculator.calculate_hours_between_dates,
        'week_calculator': week_calculator.week_number_calculator
    }

    script_choices = list(scripts.keys())
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