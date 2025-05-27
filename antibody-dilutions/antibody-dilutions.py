def calculate_dilution_with_overage(dilution_factor, num_coverslips, volume_per_coverslip_uL, overage_percent=10):
    """
    Calculate volume of stock antibody and diluent needed for IFA with pipetting overage.

    Parameters:
        dilution_factor (int): e.g., 500 for a 1:500 dilution
        num_coverslips (int): number of coverslips
        volume_per_coverslip_uL (float): volume of antibody to use per coverslip in µL
        overage_percent (float): extra volume to compensate for pipetting error (default 10%)

    Returns:
        dict with adjusted total_volume_uL, stock_volume_uL, and diluent_volume_uL
    """
    base_total_volume = num_coverslips * volume_per_coverslip_uL
    adjusted_total_volume = base_total_volume * (1 + overage_percent / 100)
    
    stock_volume_uL = adjusted_total_volume / dilution_factor
    diluent_volume_uL = adjusted_total_volume - stock_volume_uL

    return {
        'adjusted_total_volume_uL': round(adjusted_total_volume, 2),
        'stock_volume_uL': round(stock_volume_uL, 2),
        'diluent_volume_uL': round(diluent_volume_uL, 2)
    }

# Example usage:
if __name__ == "__main__":
    dilution = int(input("Enter dilution factor (e.g., 500 for 1:500): "))
    coverslips = int(input("Enter number of coverslips: "))
    vol_per_coverslip = float(input("Enter volume per coverslip in µL: "))

    result = calculate_dilution_with_overage(dilution, coverslips, vol_per_coverslip)

    print("\n--- Dilution Calculation with 10% Overage ---")
    print(f"Total volume (with overage): {result['adjusted_total_volume_uL']} µL")
    print(f"Volume of antibody stock: {result['stock_volume_uL']} µL")
    print(f"Volume of diluent (e.g., PBS): {result['diluent_volume_uL']} µL")
