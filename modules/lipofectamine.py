def calculate_lipofection_volumes(well_format, num_wells, dna_concentration_ug_per_ul=1.0):
    """
    Calculate Lipofectamine 3000 transfection reagent volumes based on well format and number of wells.
    
    Parameters:
        well_format (str): '96-well', '24-well', '12-well', or '6-well'
        num_wells (int): Number of wells to transfect
        dna_concentration_ug_per_ul (float): Concentration of your DNA stock (default is 1.0 µg/µL)

    Returns:
        dict: Reagent volumes required
    """

    protocol_table = {
        "96-well": {
            "DNA_ug": 0.1,
            "P3000_ul": 0.2,
            "Lipo3000_ul": (0.15, 0.3),
            "OptiMEM_ul": (10, 5)
        },
        "24-well": {
            "DNA_ug": 0.5,
            "P3000_ul": 1.0,
            "Lipo3000_ul": (0.75, 1.5),
            "OptiMEM_ul": (50, 25)
        },
        "12-well": {
            "DNA_ug": 1,
            "P3000_ul": 2,
            "Lipo3000_ul": (1.5, 3),
            "OptiMEM_ul": (100, 50)
        },
        "6-well": {
            "DNA_ug": 2.5,
            "P3000_ul": 5.0,
            "Lipo3000_ul": (3.75, 7.5),
            "OptiMEM_ul": (250, 125)
        }
    }

    if well_format not in protocol_table:
        raise ValueError("Invalid well format. Choose from: '96-well', '24-well', '12-well', or '6-well'")

    params = protocol_table[well_format]

    dna_total_ug = params["DNA_ug"] * num_wells
    dna_vol_ul = dna_total_ug / dna_concentration_ug_per_ul
    p3000_total_ul = params["P3000_ul"] * num_wells

    total = {
        "DNA (µL) per tube": round((dna_vol_ul / 2), 2),
        "P3000 Reagent (µL) per tube": round((p3000_total_ul / 2), 2),
        "Opti-MEM for DNA mix per tube (µL)": round((params["OptiMEM_ul"][0] * num_wells) / 2, 2),
        "Lipofectamine 3000 Reagent (µL) - Low dose": round(params["Lipo3000_ul"][0] * num_wells, 2),
        "Lipofectamine 3000 Reagent (µL) - High dose": round(params["Lipo3000_ul"][1] * num_wells, 2),
        "Opti-MEM for Lipo mix per tube (µL)": round(params["OptiMEM_ul"][1] * num_wells, 2),
        "Final complex volume per well (µL)": round((params["OptiMEM_ul"][0] + params["OptiMEM_ul"][1]) * 2, 2),
        "Total DNA (µg)": round(dna_total_ug, 2)
    }

    return total

def calculate_lipofectamine(config):
    well_format = config.get("well_format", "12-well")
    num_wells = config.get("num_wells", 12)
    dna_concentration_ug_per_ul = config.get("dna_concentration_ug_per_ul", 0.8)

    return calculate_lipofection_volumes(well_format, num_wells, dna_concentration_ug_per_ul)