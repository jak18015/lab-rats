def c1v1(c1, v1, c2, v2):
    """
    Calculate the volume of v1 or v2 based on the concentrations c1 and c2.
    Provide x as None to calculate the missing value.
    :param c1: Concentration of solution 1 (μM)
    :param v1: Volume of solution 1 (mL)
    :param c2: Concentration of solution 2 (μM)
    :param v2: Volume of solution 2 (mL)
    :return: The calculated volume (mL) or concentration (μM)
    """

    if v2 is None:
        v2 = c1 * v1 / c2
        return v2
    elif v1 is None:
        v1 = c2 * v2 / c1
        return v1
    elif c2 is None:
        c2 = c1 * v1 / v2
        return c2
    elif c1 is None:
        c1 = c2 * v2 / v1
        return c1
    else:
        raise ValueError("One of the parameters must be None to calculate the missing value.")
    
def formaldehyde(formaldehyde_stock=10, formaldehyde_dilution=4, pbs_stock=10, pbs_dilution=1, volume_final=12):
    """
    Prepare a formaldehyde solution for immunofluorescence assay (IFA).
    This function calculates the volumes of formaldehyde stock, PBS stock, and water needed to
    achieve the desired final concentrations.
    :param formaldehyde_stock: Stock solution concentration as a percentage (default is 10%)
    :param formaldehyde_dilution: Desired final concentration as a percentage (default is 4%)
    :param pbs_stock: Stock PBS solution as a multiple of 1x (default is 10xPBS)
    :param pbs_dilution: Desired final concentration as a multiple of 1x (default is 1xPBS)
    :param volume_final: Final volume of the diluted solution in mL (default is 12 mL)
    :return: Dictionary with calculated volumes
    """
    volume_stock_formaldehyde = c1v1(c1=formaldehyde_stock, v1=None, c2=formaldehyde_dilution, v2=volume_final)
    volume_stock_pbs = c1v1(c1=pbs_stock, v1=None, c2=pbs_dilution, v2=volume_final)
    volume_water = volume_final - (volume_stock_formaldehyde + volume_stock_pbs)

    return {
        "volume_stock_formaldehyde": round(volume_stock_formaldehyde, 2),
        "volume_stock_pbs": round(volume_stock_pbs, 2),
        "volume_water": round(volume_water, 2)
    }


def triton(triton_stock=10, triton_dilution=0.1, pbs_stock=10, pbs_dilution=1, volume_final=12):
    """
    Prepare a Triton X-100 solution for immunofluorescence assay (IFA).
    This function calculates the volumes of Triton X-100 stock, PBS stock, and water needed to
    achieve the desired final concentrations.
    :param triton_stock: Stock solution concentration as a percentage (default is 10%)
    :param triton_dilution: Desired final concentration as a percentage (default is 0.1%)
    :param pbs_stock: Stock PBS solution as a multiple of 1x (default is 10xPBS)
    :param pbs_dilution: Desired final concentration as a multiple of 1x (default is 1xPBS)
    :param volume_final: Final volume of the diluted solution in mL (default is 12 mL)
    :return: Dictionary with calculated volumes
    """
    volume_stock_triton = c1v1(c1=triton_stock, v1=None, c2=triton_dilution, v2=volume_final)
    volume_stock_pbs = c1v1(c1=pbs_stock, v1=None, c2=pbs_dilution, v2=volume_final)
    volume_water = volume_final - (volume_stock_triton + volume_stock_pbs)

    return {
        "volume_stock_triton": round(volume_stock_triton, 2),
        "volume_stock_pbs": round(volume_stock_pbs, 2),
        "volume_water": round(volume_water, 2)
    }


def bsa(desired_bsa_percentage=1, volume_final=12):
    """
    Prepare a Bovine Serum Albumin (BSA) solution for immunofluorescence assay (IFA).
    This function calculates the mass of BSA needed and the volumes of PBS stock and water to
    achieve the desired final concentration.
    :param desired_bsa_percentage: Desired final concentration of BSA as a percentage (default is 1%)
    :param volume_final: Final volume of the diluted solution in mL (default is 12 mL)
    :return: Dictionary with calculated mass and volumes
    """
    bsa_concentration = desired_bsa_percentage / 100
    mass_bsa = bsa_concentration * volume_final

    return {
        "mass_bsa": round(mass_bsa, 2),
        "dissolve_volume": round(volume_final / 2, 2),
        "final_volume": volume_final
    }


def ifa(formaldehyde_stock, formaldehyde_dilution, pbs_stock, pbs_dilution, volume_final,
        triton_stock, triton_dilution, desired_bsa_percentage):
    """
    Perform immunofluorescence assay (IFA) preparation.
    This function calls the formaldehyde, triton, and bsa functions to prepare the necessary solutions.
    """
    return {
        "formaldehyde": formaldehyde(formaldehyde_stock, formaldehyde_dilution, pbs_stock, pbs_dilution, volume_final),
        "triton": triton(triton_stock, triton_dilution, pbs_stock, pbs_dilution, volume_final),
        "bsa": bsa(desired_bsa_percentage, volume_final)
    }


def calculate_ifa(config):
    return ifa(
        config["formaldehyde_stock"],
        config["formaldehyde_dilution"],
        config["pbs_stock"],
        config["pbs_dilution"],
        config["volume_final"],
        config["triton_stock"],
        config["triton_dilution"],
        config["desired_bsa_percentage"]
    )


def print_ifa_results(config, results):
    print(f"\n{config['formaldehyde_dilution']}% formaldehyde solution:")
    f_res = results['formaldehyde']
    print(f"Volume of {config['formaldehyde_stock']}% formaldehyde: {f_res['volume_stock_formaldehyde']:.2f} mL.")
    print(f"Volume of {config['pbs_stock']}xPBS: {f_res['volume_stock_pbs']:.2f} mL.")
    print(f"Volume of water: {f_res['volume_water']:.2f} mL.")
    print(f"Final concentrations: Formaldehyde: {config['formaldehyde_dilution']}%, PBS: {config['pbs_dilution']}X")

    print(f"\n{config['triton_dilution']}% Triton X-100 solution:")
    t_res = results['triton']
    print(f"Total volume of the final solution: {config['volume_final']} mL.")
    print(f"Volume of Triton X-100: {t_res['volume_stock_triton']:.2f} mL.")
    print(f"Volume of {config['pbs_stock']}xPBS: {t_res['volume_stock_pbs']:.2f} mL.")
    print(f"Volume of water: {t_res['volume_water']:.2f} mL.")
    print(f"Final concentrations: Triton X-100: {config['triton_dilution']}%, PBS: {config['pbs_dilution']}X")

    print(f"\n{config['desired_bsa_percentage']}% BSA solution:")
    b_res = results['bsa']
    print(f"Total volume of the final solution: {config['volume_final']} mL.")
    print(f"Mass of BSA needed: {b_res['mass_bsa']:.2f} g.")
    print(f"Dissolve BSA in {b_res['dissolve_volume']:.2f} mL of {config['pbs_dilution']}xPBS solution.")
    print(f"Raise to {b_res['final_volume']} mL with {config['pbs_dilution']}xPBS.")
    print(f"Final concentrations: BSA: {config['desired_bsa_percentage']}% ")



# Example usage:
if __name__ == "__main__":
    c1 = 100  # Concentration of solution 1 in μM
    v1 = 10   # Volume of solution 1 in mL
    c2 = None # Concentration of solution 2 in μM (to be calculated)
    v2 = 20   # Volume of solution 2 in mL

    result = c1v1(c1, v1, c2, v2)
    print(f"The calculated concentration c2 is: {result} μM")

