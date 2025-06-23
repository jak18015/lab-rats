from c1v1 import c1v1

def triton():
    # Triton X-100 stock and desired final concentrations
    triton_stock = 10  # Stock solution concentration as a percentage (10%)
    triton_dilution = 0.1  # Desired final concentration as a percentage (0.1%)

    # PBS stock and desired final concentrations
    pbs_stock = 10  # Stock PBS solution as a multiple of 1x (10xPBS)
    pbs_dilution = 1  # Desired final concentration as a multiple of 1x (1xPBS)

    volume_final = 12  # Final volume of the diluted solution in mL

    # Calculate the volumes needed using the c1v1 formula
    volume_stock_triton = c1v1(c1=triton_stock, v1=None, c2=triton_dilution, v2=volume_final)
    volume_stock_pbs = c1v1(c1=pbs_stock, v1=None, c2=pbs_dilution, v2=volume_final)
    volume_water = volume_final - (volume_stock_triton + volume_stock_pbs)

    # Display the results
    print(f"Total volume of the final solution: {volume_final} mL.")
    print(f"Volume of Triton X-100: {volume_stock_triton:.2f} mL.")
    print(f"Volume of 10xPBS: {volume_stock_pbs:.2f} mL.")
    print(f"Volume of water: {volume_water:.2f} mL.")
    print(f"Final concentrations: Triton X-100: {triton_dilution}%, PBS: {pbs_dilution}X")

if __name__ == "__main__":
    triton()