# Lab Rats
### Common day-to-day calculations

<!-- Centered Image with Specified Width -->
<div style="text-align:center;">
    <img src="images/labrat.jpg" alt="Lab rat image" width="300"/>
</div>

### Includes
- Antibody dilution calculator (ab.py)
- Hours post-infection calculator (date_calulator.py)
- Gibson Assembly master mix volumes calculator (gibson.py)
- Fixation, permeabilization, and blocking buffers volume calculator (ifa.py)
- Lipofection volumes calculator (lipofectamine.py)
- Week number calculator (week_calculator.py)

### Installation
1. Clone the git repo `git clone https://github.com/jak18015/lab-calculations.git`
2. Run `main.py` frome the `lab-calculations/` directory.

### Modifying the configuration files for each module
- Each module has an associated config file in `configs/` that can be updated manually or interactively within the script when that module is selected.

### Adding new modules
- To add a new module:
  - Create a `module_config.json` in `configs/`
  - Create the module in `modules/` to accept the config file (e.g. `some_function(config)`)
  - Import the new module
  - Add it as a key/value pair to the scripts dictionary
