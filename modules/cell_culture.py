flask_surface_areas = {
    'T25': 25.0,
    'T75': 75.0,
    'T175': 175.0,
    '6-well': 57.6,
    '12-well': 45.6,
    '24-well': 45.6,
    '96-well': 30.72,
    '35mm': 9.6
}

def check_flask_type(initial_flask_list, final_flask_list):
    """
    Check if all flasks in the initial and final lists are valid flask types.
    :param initial_flask_list: List of initial flask types
    :param final_flask_list: List of final flask types
    :return: Tuple (is_valid, message)
    """
    for flask in initial_flask_list:
        if flask not in flask_surface_areas:
            return False, f"Error: {flask} in {initial_flask_list} is not a recognized flask type."
    for flask in final_flask_list:
        if flask not in flask_surface_areas:
            return False, f"Error: {flask} in {final_flask_list} is not a recognized flask type."        
    return True, "All flask types are valid."

def surface_area(flask_list):
    """
    Calculate the total surface area of the flasks.
    :param flask_list: List of flask types
    :return: Total surface area of the flasks
    """
    total_surface_area = 0
    for flask in flask_list:
        total_surface_area += flask_surface_areas[flask]
    return total_surface_area

def splitter(initial_flask_list, final_flask_list, split_factor):
    """
    Check if the total surface area of the initial flasks is sufficient for the final flasks after applying a split factor.
    :param initial_flask_list: List of initial flask types
    :param final_flask_list: List of final flask types
    :param split_factor: Factor by which the surface area is increased (e.g., 4 for a 1:4 split)
    :return: String indicating whether there are enough cells or if more are needed, along with the excess or deficit surface area.
    """
    if check_flask_type(initial_flask_list, final_flask_list)[0] is False:
        return check_flask_type(initial_flask_list, final_flask_list)[1]
    total_initial_surface_area = surface_area(initial_flask_list)
    effective_surface_area = total_initial_surface_area * split_factor
    required_surface_area = surface_area(final_flask_list)
    surface_area_difference = effective_surface_area - required_surface_area
    if surface_area_difference >= 0:
        return f"You have enough cells. Excess surface area: {surface_area_difference:.2f} cm²."
    else:
        return f"Insufficient cells. Need additional surface area: {abs(surface_area_difference):.2f} cm²."

def calculate_cell_culture(config):
    """
    Process a configuration dictionary to perform flask splitting.
    :param config: Dictionary containing initial and final flask lists and split factor
    :return: Result of the flask split operation
    """
    initial_flasks = config.get("initial_flasks", [])
    final_flasks = config.get("final_flasks", [])
    split_factor = config.get("split_factor", 4)

    return splitter(initial_flasks, final_flasks, split_factor)

# Example usage
if __name__ == "__main__":
    # Example configuration
    config = {
        "initial_flasks": ['T25'],
        "final_flasks": ['T75'],
        "split_factor": 3
    }
    initial_flasks = config.get("initial_flasks", [])
    final_flasks = config.get("final_flasks", [])
    split_factor = config.get("split_factor", 4)

    result = splitter(initial_flasks, final_flasks, split_factor)
    print(result)