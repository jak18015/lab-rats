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
    

# Example usage:
if __name__ == "__main__":
    c1 = 100  # Concentration of solution 1 in μM
    v1 = 10   # Volume of solution 1 in mL
    c2 = None # Concentration of solution 2 in μM (to be calculated)
    v2 = 20   # Volume of solution 2 in mL

    result = c1v1(c1, v1, c2, v2)
    print(f"The calculated concentration c2 is: {result} μM")