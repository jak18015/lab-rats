import os, json

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