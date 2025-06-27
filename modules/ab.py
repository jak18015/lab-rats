def calculate_multi_dilution(num_coverslips, volume_per_coverslip_uL, antibodies, overage_percent=10):
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


def calculate_ab(config):
    coverslips = config["num_coverslips"]
    vol_per_coverslip = config["volume_per_coverslip_uL"]
    overage = config.get("overage_percent", 10)
    dilution_sets = config["dilution_sets"]

    results = {}
    for set_name, antibodies in dilution_sets.items():
        results[set_name] = calculate_multi_dilution(coverslips, vol_per_coverslip, antibodies, overage)
    
    return results

def print_ab_results(config, results):
    coverslips = config["num_coverslips"]
    vol_per_coverslip = config["volume_per_coverslip_uL"]
    overage = config.get("overage_percent", 10)

    print("\n=== Antibody Dilution Calculations ===\n")
    print(f"Number of coverslips: {coverslips}")
    print(f"Volume per coverslip: {vol_per_coverslip} µL")
    print(f"Overage percentage: {overage}%\n")

    for set_name, result in results.items():
        print(f"--- {set_name} ---")
        print(f"Total volume: {result['adjusted_total_volume_uL']} µL")
        for name, vol in result['stock_volumes_uL'].items():
            print(f"\t- {name}: {vol} µL")
        print(f"\t- 1% BSA: {result['diluent_volume_uL']} µL\n")