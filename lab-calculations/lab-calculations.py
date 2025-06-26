import os
import json
from modules import ab, ifa

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
    def prompt_for_value(prefix, key, value):
        if isinstance(value, dict):
            print(f"\nEditing dictionary for '{prefix}{key}':")
            for subkey, subval in value.items():
                # Recursively handle nested dictionaries
                new_subval = prompt_for_value(f"{prefix}{key}.", subkey, subval)
                value[subkey] = new_subval
        else:
            full_key = f"{prefix}{key}"
            new_value = input(f"Enter new value for {full_key} (current: {value}, press Enter to keep current): ").strip()
            if new_value:
                try:
                    # Convert the value to the appropriate type
                    if isinstance(value, int):
                        return int(new_value)
                    elif isinstance(value, float):
                        return float(new_value)
                    else:
                        return new_value  # For strings or other types
                except ValueError:
                    print(f"Invalid input for {full_key}, keeping original value.")
            return value

        return value

    for key, value in config.items():
        config[key] = prompt_for_value("", key, value)

def main():
    if not os.getcwd().endswith("lab-calculations"):
        raise RuntimeError("Please run this script from the 'lab-calculations' directory.")

    scripts = {
        'ab': ab.calculate_ab_dilutions,
        'ifa': ifa.c1v1_calculator,
    }
    configs = {
        'ab': 'configs/ab_config.json',
        'ifa': 'configs/ifa_config.json',
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