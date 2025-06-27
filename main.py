import os
import argparse
import importlib
from modules.config_functions import load_config, save_config, edit_config

def discover_modules():
    scripts = {}
    modules_dir = "modules"
    for filename in os.listdir(modules_dir):
        if filename.endswith(".py") and not filename.startswith("__") and filename != "config_functions.py":
            module_name = filename[:-3]
            module = importlib.import_module(f"modules.{module_name}")
            
            # Convention: calculation function is named after the module
            # and print function is named print_<module_name>_results
            calc_func_name = f"calculate_{module_name}"
            print_func_name = f"print_{module_name}_results"

            if hasattr(module, calc_func_name):
                calc_func = getattr(module, calc_func_name)
                print_func = getattr(module, print_func_name, lambda c, r: print(r))
                scripts[module_name] = (calc_func, print_func)
            elif hasattr(module, module_name): # fallback for simple modules
                scripts[module_name] = (getattr(module, module_name), lambda c, r: print(r))


    return scripts

def main():
    """Run the script selected by the user."""
    scripts = discover_modules()
    parser = argparse.ArgumentParser(description='Run common lab calculations.')
    parser.add_argument('script', choices=scripts.keys(), help='The calculation to run.')

    args, remaining_argv = parser.parse_known_args()

    script_name = args.script
    config = load_config(script_name)

    if not remaining_argv:
        # Interactive mode
        print(f"Running {script_name} in interactive mode...")
        edit_config(config)
        if input("Do you want to save the updated configuration? (y/n): ").strip().lower() == 'y':
            save_config(script_name, config)
    else:
        # Command-line mode
        config_parser = argparse.ArgumentParser(description=f'Arguments for {script_name}')
        for key, value in config.items():
            if isinstance(value, bool):
                config_parser.add_argument(f'--{key}', action='store_true')
            else:
                config_parser.add_argument(f'--{key}', type=type(value), default=value)
        config_args = config_parser.parse_args(remaining_argv)
        config.update(vars(config_args))

    calculation_func, print_func = scripts[script_name]
    results = calculation_func(config)
    print_func(config, results)

if __name__ == "__main__":
    main()