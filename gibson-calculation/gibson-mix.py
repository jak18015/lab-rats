import os

def scale_gibson_mastermix(num_reactions, hot_fusion=False):
    """Scale Gibson Assembly Master Mix ingredients based on desired number of reactions."""

    base_reactions = 40
    scale_factor = num_reactions / base_reactions

    recipe = {
        "5x Isothermal reaction buffer": 160.0,
        "1/10 T5 exonuclease (1U/uL)": 3.2,
        "Phusion DNA polymerase (2U/uL)": 10.0,
        "Taq DNA ligase (40U/uL)": 80.0,
        "Molecular biology grade H2O": 346.8
    }

    if hot_fusion:
        # Remove ligase and reassign its volume to water
        ligase_volume = recipe.pop("Taq DNA ligase (40U/uL)")
        recipe["Molecular biology grade H2O"] += ligase_volume

    scaled_recipe = {}
    adjustments = {}

    for ingredient, amount in recipe.items():
        scaled_amount = round(amount * scale_factor, 2)
        if scaled_amount < 1.0:
            adjustments[ingredient] = scaled_amount
            scaled_amount = 1.0
        scaled_recipe[ingredient] = scaled_amount

    scaled_recipe["Total volume (uL)"] = round(sum(scaled_recipe.values()), 2)
    scaled_recipe["Aliquot size (uL)"] = 15
    scaled_recipe["Number of aliquots"] = int(scaled_recipe["Total volume (uL)"] // 15)

    return scaled_recipe, adjustments, hot_fusion

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Get user input
num_reactions = input("Enter the number of reactions: ")
try:
    num_reactions = int(num_reactions)
    if num_reactions <= 0:
        raise ValueError("Number of reactions must be a positive integer.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit(1)

hot_fusion_input = input("Use Hot Fusion (no ligase)? (y/n): ").strip().lower()
hot_fusion = hot_fusion_input == 'y'

# Scale and get adjustments
scaled, adjustments, hot_fusion_used = scale_gibson_mastermix(num_reactions, hot_fusion)

# Print header
print(f"\nScaled {'Hot Fusion' if hot_fusion_used else 'Gibson'} Assembly Master Mix for {num_reactions} reactions:")
print(f"Total volume: {scaled['Total volume (uL)']} μL")
print(f"Aliquot size: {scaled['Aliquot size (uL)']} μL")

# Print ingredients with aligned formatting
print("\nScaled Ingredients:")
ingredient_keys = [k for k in scaled if "volume" not in k and "Aliquot" not in k]
max_key_len = max(len(k) for k in ingredient_keys)

for ingredient in ingredient_keys:
    print(f"{ingredient:<{max_key_len}} : {scaled[ingredient]} μL")

# Print adjustment notes
if adjustments:
    print("\nNote:")
    for ingredient, original_value in adjustments.items():
        print(f"- {ingredient}: originally {original_value} μL, raised to 1.0 μL for pipetting accuracy.")

if hot_fusion_used:
    print("\nHot Fusion mode: Taq DNA ligase omitted and volume replaced with water.")
