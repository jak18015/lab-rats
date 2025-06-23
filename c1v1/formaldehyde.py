from c1v1 import c1v1

def formaldehyde():
      formaldehyde_stock = 10  # Stock solution concentration as a percentage (10%)
      formaldehyde_dilution = 4  # Desired final concentration as a percentage (4%)

      pbs_stock = 10 # Stock PBS solution as a multiple of 1x (10xPBS)
      pbs_dilution = 1  # Desired final concentration as a multiple of 1x (1xPBS)

      volume_final = 12  # Final volume of the diluted solution in mL

      # Calculate the volumes needed using the c1v1 formula
      volume_stock_formaldehyde = c1v1(c1=formaldehyde_stock, v1=None, c2=formaldehyde_dilution, v2=volume_final)
      volume_stock_pbs = c1v1(c1=pbs_stock, v1=None, c2=pbs_dilution, v2=volume_final)
      volume_water = volume_final - (volume_stock_formaldehyde + volume_stock_pbs)

      print(f"Volume of 10% formaldehyde: {volume_stock_formaldehyde:.2f} mL.")
      print(f"Volume of 10xPBS: {volume_stock_pbs:.2f} mL.")
      print(f"Volume of water: {volume_water:.2f} mL.")
      print(f"Final concentrations: Formaldehyde: {formaldehyde_dilution}%, PBS: {pbs_dilution}X")


if __name__ == "__main__":
    formaldehyde()
