from modules.c1v1 import formaldehyde, triton, bsa


def ifa(formaldehyde_stock, formaldehyde_dilution, pbs_stock, pbs_dilution, volume_final,
        triton_stock, triton_dilution, desired_bsa_percentage):
    """
    Perform immunofluorescence assay (IFA) preparation.
    This function calls the formaldehyde, triton, and bsa functions to prepare the necessary solutions.
    """
    print(f"\n{formaldehyde_dilution}% formaldehyde solution:")
    formaldehyde(formaldehyde_stock, formaldehyde_dilution, pbs_stock, pbs_dilution, volume_final)
    print(f"\n{triton_dilution}% Triton X-100 solution:")
    triton(triton_stock, triton_dilution, pbs_stock, pbs_dilution, volume_final)
    print(f"\n{desired_bsa_percentage}% BSA solution:")
    bsa(desired_bsa_percentage, volume_final)


if __name__ == "__main__":
    formaldehyde_stock = 10  # Stock solution concentration as a percentage
    formaldehyde_dilution = 4  # Desired final concentration as a percentage
    pbs_stock = 10  # Stock PBS solution as a multiple of 1x
    pbs_dilution = 1  # Desired final concentration as a multiple of 1x
    volume_final = 12  # Final volume of the solutions in mL
    triton_stock = 10  # Stock solution concentration as a percentage
    triton_dilution = 0.025  # Desired final concentration as a percentage
    desired_bsa_percentage = 1  # Desired final concentration as a percentage

    ifa(formaldehyde_stock, formaldehyde_dilution, pbs_stock, pbs_dilution, volume_final,
        triton_stock, triton_dilution, desired_bsa_percentage)