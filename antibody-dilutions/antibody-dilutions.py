import os

def calculate_multi_dilution(num_coverslips, volume_per_coverslip_uL, antibodies, overage_percent=10):
    """
    Calculate stock and diluent volumes for multiple antibodies in IFA.

    Parameters:
        num_coverslips (int): number of coverslips
        volume_per_coverslip_uL (float): volume to use per coverslip
        antibodies (dict): dictionary with antibody names as keys and dilution factors as values
        overage_percent (float): extra volume to compensate for pipetting error

    Returns:
        dict with total volume, antibody stock volumes, and required diluent
    """
    base_total_volume = num_coverslips * volume_per_coverslip_uL
    adjusted_total_volume = base_total_volume * (1 + overage_percent / 100)

    stock_volumes = {}
    total_stock_volume = 0.0

    for ab_name, dilution in antibodies.items():
        stock_vol = adjusted_total_volume / dilution
        stock_volumes[ab_name] = round(stock_vol, 2)
        total_stock_volume += stock_vol

    diluent_volume = round(adjusted_total_volume - total_stock_volume, 2)

    return {
        'adjusted_total_volume_uL': round(adjusted_total_volume, 2),
        'stock_volumes_uL': stock_volumes,
        'diluent_volume_uL': diluent_volume
    }

# Example usage:
if __name__ == "__main__":
    os.system('clear')
    coverslips = int(input("Enter number of coverslips: "))
    vol_per_coverslip = float(input("Enter volume per coverslip in µL: "))
    num_antibodies = int(input("Enter number of antibodies to include: "))

    antibodies = {}
    for i in range(num_antibodies):
        name = input(f"Enter name of antibody #{i + 1}: ")
        dilution = int(input(f"Enter dilution factor for {name} (e.g., 500 for 1:500): "))
        antibodies[name] = dilution

    result = calculate_multi_dilution(coverslips, vol_per_coverslip, antibodies)

    print("\n--- Multi-Antibody Dilution Calculation with 10% Overage ---")
    print(f"Total volume (with overage): {result['adjusted_total_volume_uL']} µL")
    for name, vol in result['stock_volumes_uL'].items():
        print(f"Volume of {name} stock: {vol} µL")
    print(f"Volume of diluent (e.g., PBS): {result['diluent_volume_uL']} µL")
